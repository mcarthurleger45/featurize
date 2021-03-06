import React, { Component } from 'react';
import Nav from './components/nav';
import LoginForm from './components/Register/loginform';
import SignupForm from './components/Register/signupform';
import './App.css';
import {AUTHENTICATION_API, TOKEN_API} from './endpoints';
import {getCookie} from './utils';
import FeatureRequestList from './components/FeatureRequest/list';

class MyApp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      displayed_form: '',
      logged_in: localStorage.getItem('token') ? true : false,
      user: ''
    };
  }

  componentDidMount() {
    if (this.state.logged_in) {
      fetch(AUTHENTICATION_API, {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`
        }
      })
        .then(res => res.json())
        .then(json => {
          this.setState({ user: json });
        });
    }
  }

  handle_login = (e, data) => {
    e.preventDefault();
    fetch(TOKEN_API, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(json => {
        localStorage.setItem('token', json.token);
        this.setState({
          logged_in: true,
          displayed_form: '',
          user: json.user
        });
      });
  };

  handle_signup = (e, data) => {
    e.preventDefault();
    const csrf = getCookie('csrftoken')
    fetch(AUTHENTICATION_API, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf,
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(json => {
        localStorage.setItem('token', json.token);
        this.setState({
          logged_in: true,
          displayed_form: '',
          user: json.user
        });
      });
  };

  handle_logout = () => {
    localStorage.removeItem('token');
    this.setState({ logged_in: false, username: '' });
  };

  display_form = form => {
    this.setState({
      displayed_form: form
    });
  };

  render() {
    let form;
    switch (this.state.displayed_form) {
      case 'login':
        form = <LoginForm handle_login={this.handle_login} />;
        break;
      case 'signup':
        form = <SignupForm handle_signup={this.handle_signup} />;
        break;
      default:
        form = null;
    }
    const requests = (this.state.logged_in) ? <FeatureRequestList user={this.state.user} />: '';

    return (
      <div className="App">
        <Nav
          logged_in={this.state.logged_in}
          display_form={this.display_form}
          handle_logout={this.handle_logout}
        />
        {form}
        <h3>
          {this.state.logged_in
            ? `Hello, ${this.state.user.username}`
            : 'Please Log In'}
        </h3>
        {requests}
      </div>
    );
  }
}

export default MyApp;