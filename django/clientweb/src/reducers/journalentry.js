import { GET_JOURNALENTRY, DELETE_JOURNALENTRY, ADD_JOURNALENTRY, CLEAR_JOURNALENTRY } from '../actions/types.js';

const initialState = {
  journalentry: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_JOURNALENTRY:
      return {
        ...state,
        journalentry: action.payload,
      };
    case DELETE_JOURNALENTRY:
      return {
        ...state,
        journalentry: state.journalentry.filter((journalentry) => journalentry.id !== action.payload),
      };
    case ADD_JOURNALENTRY:
      return {
        ...state,
        journalentry: [...state.journalentry, action.payload],
      };
    case CLEAR_JOURNALENTRY:
      return {
        ...state,
        journalentry: [],
      };
    default:
      return state;
  }
}
