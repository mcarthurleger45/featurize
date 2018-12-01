import React, { Component } from 'react';
import { FEATURED_REQUEST_API, AUTHENTICATION_API } from '../../endpoints';
import FeatureRequest from './item';
import './list.css';
import PropTypes from 'prop-types';

class FeatureRequestList extends Component {
    constructor(props){
        super(props);
        this.state = {
            data: [],
        };
    }

    componentDidMount(){
        const userId = this.props.user.id != null ? this.props.user.id : '';
        const url = AUTHENTICATION_API + userId;
        fetch(url, {
            headers: {
              Authorization: `JWT ${localStorage.getItem('token')}`
            }}) 
            .then(response => response.json())
            .then(data => this.setState({ data: data.feature_requests }));
    }

    render(){
        const showActions = this.props.user != null;
        const featureList = (this.state.data) ?this.state.data.map((featureRequest, i) => <FeatureRequest data={featureRequest} key={i} showActions={showActions} /> ): <div> --- </div>;
        return (
            <div className='featureRequest-list'>
                {featureList}
            </div>
        )
    }
}

FeatureRequestList.propTypes = {
    user: PropTypes.string.isRequired,
};

export default FeatureRequestList;