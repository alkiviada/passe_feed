import {combineReducers} from "redux";

import feedReducer from "./feedReducers";

export default combineReducers({
  feed: feedReducer,
});
