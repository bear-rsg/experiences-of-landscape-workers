import React, { Fragment } from 'react';
import { HashRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
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
