import { FETCH_ITEMS, FETCH_ITEMS_FULFILLED, FETCH_ITEMS_REJECTED } from '../actions/types';

const initialState = {
  items: [],
  error: null,
  fetching: false,
  fetched: false,
};

export default function(state = initialState, action) {
  switch (action.type) {
    case FETCH_ITEMS: return { ...state, 
                               fetching: true, 
                             };
    case FETCH_ITEMS_FULFILLED: return { ...state, 
                                         error: null, 
                                         fetched: true,
                                         fetching: false,
                                         items: action.payload, 
                                       };
    case FETCH_ITEMS_REJECTED: return { ...state, fetching: false, 
                                        error: action.payload, 
                                      };
    default:
      return state;
  }
}

