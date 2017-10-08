import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

export default class NavBar extends Component {
    componentWillMount() {
        axios.get('/check_logged_in').then(function(res) {
            console.log(res);
        })
            .catch(function(err) {
                console.log(err);
            })
    }

    render() {
        return (
            <nav className="navbar navbar-default">
              <div className="container-fluid">
                <div className="navbar-header">
                  <button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span className="sr-only">Toggle navigation</span>
                    <span className="icon-bar"></span>
                    <span className="icon-bar"></span>
                    <span className="icon-bar"></span>
                  </button>
                  <a className="navbar-brand" href="#">CalHacks, 2017</a>
                </div>
                  <div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                  <ul className="nav navbar-nav">
                    <li className="active"><a href="#">Contacts <span className="sr-only">(current)</span></a></li>
                    <li><a href="#">Interactions</a></li>
                    <li><a href='#'>Blah</a></li>
                  </ul>
                      <ul class="nav navbar-nav navbar-right">
                          <li><a href="#">Link</a></li>
                      </ul>
                </div>
              </div>
            </nav>
        );
    }
};