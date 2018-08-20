import React, { Component } from 'react';
import axios from 'axios';
import {Button, ControlLabel, FormControl, FormGroup, HelpBlock, Radio} from 'react-bootstrap'

export default class AircraftMaintenance extends React.Component {

    state = {
        maintenance: []
    }

    componentDidMount() {
        this.refreshHistory()
    }

    componentDidUpdate = (prevProps, prevState, snapshot) => {
        if (prevProps.aircraft_id === undefined || prevProps.aircraft_id !== this.props.aircraft_id) {
            this.refreshHistory()
        }

        if (prevProps.update_id !== this.props.update_id) {
            this.refreshHistory()
        }
    }

    refreshHistory = () => {
        axios.get(`api/maintenance/aircraft/${this.props.aircraft_id}`)
            .then(res => {
                const maintenance = res.data;
                this.setState({ maintenance });
            })
    }

    markAsCompleted = (maintenance_id) => {
        axios.put(`api/maintenance/completed/${maintenance_id}`, {})
            .then(res => {
                this.refreshHistory()
            })
    }

    render() {
        return (
            <div>

            <table className="table table-striped table-bordered">
                <thead>
                <tr>
                    <th>Id</th>
                    <th>Description</th>
                    <th>Created</th>
                    <th>Created By</th>
                    <th>Blocking Flight</th>
                    <th>Completed</th>
                </tr>
                </thead>
                <tbody>
                {this.state.maintenance && this.state.maintenance.length === 0 ? <tr><td colSpan="6">No Maintenance History</td></tr> : null }
                { this.state.maintenance.map(item =>
                    <tr key={item.maintenance_id}>
                        <td>{item.maintenance_id}</td>
                        <td>{item.description}</td>
                        <td>{item.created}</td>
                        <td>{item.created_by}</td>
                        <td>{item.blocked ? 'Yes' : 'No'}</td>
                        <td>
                            {item.completed ? 'Yes' : 'No'}
                            {!item.completed ?  <Button type="submit" onClick={() => this.markAsCompleted(item.maintenance_id)}>Mark as Completed</Button> : null }
                        </td>
                    </tr>)
                }
                </tbody>
            </table>
            </div>
        )
    }
}

