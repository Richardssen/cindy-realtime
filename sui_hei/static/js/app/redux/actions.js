export const SET_CURRENT_USER = "SET_CURRENT_USER";

const CONNECT = "CONNECT";
const DISCONNECT = "DISCONNECT";
const GET_ALL_VIEWER = "GET_ALL_VIEWER";

export const INTERNAL_ACTIONS = {
  CONNECT: CONNECT,
  DISCONNECT: DISCONNECT,
  GET_ALL_VIEWER: GET_ALL_VIEWER
};

const UPDATE_ONLINE_VIEWER_COUNT = "UPDATE_ONLINE_VIEWER_COUNT";
const ADD_ONLINE_USER = "ADD_ONLINE_USER";
const REMOVE_ONLINE_USER = "REMOVE_ONLINE_USER";

export const EXTERNAL_ACTIONS = {
  UPDATE_ONLINE_VIEWER_COUNT: UPDATE_ONLINE_VIEWER_COUNT,
  ADD_ONLINE_USER: ADD_ONLINE_USER,
  REMOVE_ONLINE_USER: REMOVE_ONLINE_USER
};

export const setCurrentUser = user => ({
  type: SET_CURRENT_USER,
  currentUser: user
});

export const socketConnect = () => ({
  type: CONNECT
});

export const socketDisconnect = () => ({
  type: DISCONNECT
});
