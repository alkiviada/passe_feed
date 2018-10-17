import { 
  FETCH_ITEMS, 
  FETCH_ITEMS_FULFILLED, 
  FETCH_ITEMS_REJECTED, 
  } from './types';

export const fetchItems = (oldData) => dispatch => {
  console.log('fetching items');
  const url = 'api/feed/'
  fetch(url)
  .then(response =>
      response.json().then(json => ({
        status: response.status,
        json
      })
    ))
  .then(
      // Both fetching and parsing succeeded!
      ({ status, json }) => {
        if (status >= 400) {
          // Status looks bad
          console.log('Server returned error status');
          dispatch({type: FETCH_ITEMS_REJECTED, payload: {error: 'fetching items failed'}})
        } else {
      console.log(json)
      dispatch({
        type: FETCH_ITEMS_FULFILLED,
        payload: [...oldData, ...json]
      })
    }
      },
      // Either fetching or parsing failed!
      err => {
        console.log('problems');
        dispatch({type: FETCH_WORDS_REJECTED, payload: {error: 'fetching words failed'}})
      }
    ); 
};
