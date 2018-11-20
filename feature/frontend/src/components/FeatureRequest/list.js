import React, { Component } from 'react';
import { FEATURED_REQUEST_API } from '../../endpoints';
import FeatureRequest from './item';
import './style.css'

class FeatureRequestList extends Component {
    constructor(props){
        super(props);
        this.state = {
            data: [],
        };
    }

    componentDidMount(){
        fetch(FEATURED_REQUEST_API)
            .then(response => response.json())
            .then(data => this.setState({ data }));
    }

    render(){
        return (
            <div className='featuredRequestList'>
                { this.state.data.map((i, featureRequest) => <FeatureRequest data={featureRequest} key={i} /> ) }
            </div>
        )
    }
}

export default FeatureRequestList;