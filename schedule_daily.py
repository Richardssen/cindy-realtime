'''isort:skip_file'''
import os
import logging
import yaml
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cindy.settings")

import django
django.setup()
from django.utils import timezone
from django.utils.timezone import timedelta

from sui_hei.models import Award, ChatMessage, ChatRoom, Puzzle, User, DirectMessage

BASE_DIR = os.path.split(os.path.abspath(__file__))[0]
SCHEDULE_SETTING_PATH = os.path.join(BASE_DIR, './schedule_settings.yml')

logger = logging.getLogger(name=__file__)
logging.basicConfig(datefmt="%Y/%m/%d %H:%M:%S", level=logging.DEBUG)


def clean_recent_minichat(chatroomName="lobby", recent=None):
    cr = ChatRoom.objects.get(name=chatroomName)
    cr_messages = cr.chatmessage_set.order_by("id")
    count = cr_messages.count()

    logger.debug(f"[ChatRoom:{chatroomName}]: Total count: {count}")
    if not isinstance(recent, int):
        logger.debug(f"[ChatRoom:{chatroomName}]: Delete all objects")
        cr.chatmessage_set.delete()
    else:
        logger.debug(f"[ChatRoom:{chatroomName}]: Leaving message count: {recent}")

    if count <= recent:
        return

    try:
        earliest = cr_messages[count - recent - 1].id
    except IndexError:
        return

    to_delete = cr_messages.filter(id__lte=earliest)
    logger.debug(
        f"[ChatRoom:{chatroomName}]: Deleting {to_delete.count()} objects"
    )

    to_delete.delete()


def clean_recent_directmessages(recent=90):
    now = timezone.now()
    recent_days_ago = now - timedelta(days=recent)
    outdated = DirectMessage.objects.filter(created__lt=recent_days_ago)
    logger.debug(
        "[DirectMessage]: Reserve messages in recent %d days" % recent)
    logger.debug(f"[DirectMessage]: Deleting {outdated.count()} objects")
    outdated.delete()


def mark_puzzle_as_dazed():
    now = timezone.datetime.date(timezone.now())
    unsolved = Puzzle.objects.filter(status=0, dazed_on__lte=now)
    for dazed_puzzle in unsolved:
        logger.debug("[Puzzle]: Mark dazed: %d - %s" % (dazed_puzzle.id,
                                                        dazed_puzzle.title))
        dazed_puzzle.status = 2
        dazed_puzzle.modified = timezone.now()
        dazed_puzzle.save()


if __name__ == "__main__":
    settings = {}
    if os.path.exists(SCHEDULE_SETTING_PATH):
        with open(SCHEDULE_SETTING_PATH) as f:
            settings = yaml.load(f)

    # delete old minichat chat messages
    for chatroomName, recent in settings.get(
            'chatroom_messages_preserve_count', {}).items():
        clean_recent_minichat(chatroomName, recent)

    # delete old direct messages
    recent = settings.get('direct_message_preserve_days', None)
    if isinstance(recent, int):
        clean_recent_directmessages(recent)

    # mark dazed puzzles
    mark_puzzle_as_dazed()
