import axios from 'axios';
import { createMessage, returnErrors } from './messages';
import { tokenConfig } from './auth';

import { GET_JOURNALENTRY, DELETE_JOURNALENTRY, ADD_JOURNALENTRY } from './types';

// GET JOURNALENTRY
export const getJournalEntry = () => (dispatch, getState) => {
  axios
    .get('/api/journalentry/', tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_JOURNALENTRY,
        payload: res.data,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};

// DELETE JOURNALENTRY
export const deleteJournalEntry = (id) => (dispatch, getState) => {
  axios
    .delete(`/api/journalentry/${id}/`, tokenConfig(getState))
    .then((res) => {
      dispatch(createMessage({ deleteJournalEntry: 'JournalEntry Deleted' }));
      dispatch({
        type: DELETE_JOURNALENTRY,
        payload: id,
      });
    })
    .catch((err) => console.log(err));
};

// ADD JOURNALENTRY
export const addJournalEntry = (journalentry) => (dispatch, getState) => {
  axios
    .post('/api/journalentry/', journalentry, tokenConfig(getState))
    .then((res) => {
      dispatch(createMessage({ addJournalEntry: 'JournalEntry Added' }));
      dispatch({
        type: ADD_JOURNALENTRY,
        payload: res.data,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};
