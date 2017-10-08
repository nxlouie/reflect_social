import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import NavBar from './common/NavBar';
import InteractionForm from './Interactions';
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../css/main.css';

class Hello extends Component {
    render() {
        return (<div className='container-fluid'>
            <NavBar/>
            <InteractionForm/>
        </div>);
    }
}

ReactDOM.render(<Hello />, document.getElementById('container'));