import React, { Fragment } from 'react';
import Form from './Form';
import JournalEntry from './JournalEntry';

export default function Dashboard() {
  return (
    <Fragment>
      <Form />
      <JournalEntry />
    </Fragment>
  );
}
