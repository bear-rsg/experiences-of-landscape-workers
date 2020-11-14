import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getJournalEntry, deleteJournalEntry } from '../../actions/journalentry';

export class JournalEntryList extends Component {
  static propTypes = {
    journalentry: PropTypes.array.isRequired,
    getJournalEntry: PropTypes.func.isRequired,
    deleteJournalEntry: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.getJournalEntry();
  }

  render() {
    return (
      <Fragment>
        <h2>JournalEntry</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Title</th>
              <th>Entry Text</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.journalentry.map((journalentry) => (
              <tr key={journalentry.id}>
                <td>{journalentry.id}</td>
                <td>{journalentry.title}</td>
                <td>{journalentry.entry_text}</td>
                <td>
                  <button
                    onClick={this.props.deleteJournalEntry.bind(this, journalentry.id)}
                    className="btn btn-danger btn-sm"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  journalentry: state.journalentry.journalentry,
});

export default connect(mapStateToProps, { getJournalEntry, deleteJournalEntry })(JournalEntryList);
