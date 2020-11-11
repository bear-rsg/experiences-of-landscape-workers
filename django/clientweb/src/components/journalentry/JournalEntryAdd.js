import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addJournalEntry } from '../../actions/journalentry';

export class JournalEntryAdd extends Component {
  state = {
    title: '',
    entry_text: ''
  };

  static propTypes = {
    addJournalEntry: PropTypes.func.isRequired,
  };

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  onSubmit = (e) => {
    e.preventDefault();
    const { title, entry_text } = this.state;
    const journalentry = { title, entry_text };
    this.props.addJournalEntry(journalentry);
    // Clear state
    this.setState({
      title: '',
      entry_text: ''
    });
  };

  render() {
    const { title, entry_text } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Add JournalEntry</h2>
        <form onSubmit={this.onSubmit}>
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

export default connect(null, { addJournalEntry })(JournalEntryAdd);
