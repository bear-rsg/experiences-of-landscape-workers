import { combineReducers } from 'redux';
import journalentry from './journalentry';
import errors from './errors';
import messages from './messages';
import auth from './auth';

export default combineReducers({
  journalentry,
  errors,
  messages,
  auth,
});
