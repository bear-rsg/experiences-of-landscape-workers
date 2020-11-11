import React, { Fragment } from 'react';
import JournalEntryAdd from './JournalEntryAdd';
import JournalEntryUpdate from './JournalEntryUpdate';
import JournalEntryList from './JournalEntryList';

export default function Dashboard() {
  return (
    <Fragment>
      <JournalEntryAdd />
      <JournalEntryList />
      <JournalEntryUpdate />
    </Fragment>
  );
}
