import React, {Component} from 'react';

const TAGS = [
    { id: 1, name: 'Career'},
    { id: 2, name: 'Social'},
    { id: 3, name: 'Family'},
    { id: 4, name: 'Dating'},
    { id: 5, name: 'Obligation'},
    { id: 6, name: 'Worthwhile'},
    { id: 7, name: 'Time Waste'}, 
];
const SELECTED = '#2aabd2';
const NOT_SELECTED = '#2b669a';

class InteractionForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            firstName: '',
            lastName: '',
            tags: [],
            selected: [false, false, false, false, false, false, false],
            note: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.toggleTag = this.toggleTag.bind(this);
        this.getColor = this.getColor.bind(this);
    }

    toggleTag(idx) {
        const selected = this.state.selected;
        selected[idx] = !selected[idx];
        this.setState({ selected });
    }

    handleChange(event) {
        const target = event.target;
        const value = target.value;
        const name = target.name;

        this.setState({
            [name]: value
        });
    }

    handleSubmit(event) {

    }

    getColor(idx) {
        const selected = this.state.selected[idx];
        return selected? SELECTED : NOT_SELECTED;
    }

    render() {
        return (
            <div class='col-sm-8 col-sm-offset-2 interaction-form'>
                <form>
                    <div className='form-group'>
                        <label>First Name:</label>
                        <input name='firstName'
                                type='text'
                                className='form-control'
                                placeholder='First Name'
                                value={this.state.firstName}
                                onChange={this.handleChange} />
                    </div>
                    <div className='form-group'>
                        <label>Last Name:</label>
                        <input name='lastName'
                                type='text'
                                className='form-control'
                                placeholder='Last Name'
                                value={this.state.lastName}
                                onChange={this.handleChange} />
                    </div>
                    <div>
                        {
                            TAGS.map((tag, idx) => {
                                return (
                                    <div className='tag'>
                                        <div className='tag-inner'
                                             style={{ borderColor: this.getColor(idx), backgroundColor: this.getColor(idx)}}
                                             onClick={() => {this.toggleTag(idx)}}> {tag.name} </div>
                                    </div>
                                )
                            })
                        }
                    </div>
                    <div className='clearfix' />
                    <div className='form-group'>
                        <label>Notes:</label>
                        <textarea name='notes'
                                type='text'
                                className='form-control'
                                placeholder='Add your comments...'
                                value={this.state.note}
                                onChange={this.handleChange} />
                    </div>
                    <button className='btn btn-primary'>Submit</button>
                </form>
            </div>
        )
    }
}

export default InteractionForm;

