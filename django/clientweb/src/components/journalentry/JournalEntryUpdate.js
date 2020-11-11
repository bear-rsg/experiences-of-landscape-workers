import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { updateJournalEntry } from '../../actions/journalentry';

export class JournalEntryUpdate extends Component {
  state = {
    id: '',
    title: '',
    entry_text: ''
  };

  static propTypes = {
    updateJournalEntry: PropTypes.func.isRequired,
  };

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  onSubmit = (e) => {
    e.preventDefault();
    const { id, title, entry_text } = this.state;
    const journalentry = { id, title, entry_text };
    this.props.updateJournalEntry(journalentry);
    // Clear state
    this.setState({
      id: '',
      title: '',
      entry_text: ''
    });
  };

  render() {
    const { id, title, entry_text } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Update JournalEntry</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>ID</label>
            <input
              className="form-control"
              type="text"
              name="id"
              onChange={this.onChange}
              value={id}
            />
          </div>
          <div className="form-group">
            <label>Title</label>
            <input
              className="form-control"
              type="text"
              name="title"
              onChange={this.onChange}
              value={title}
            />
          </div>
          <div className="form-group">
            <label>Text</label>
            <textarea
              className="form-control"
              name="entry_text"
              onChange={this.onChange}
              value={entry_text}
            />
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(null, { updateJournalEntry })(JournalEntryUpdate);
