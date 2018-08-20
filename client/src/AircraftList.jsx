import React from 'react';
import axios from 'axios';

export default class AircraftList extends React.Component {

    state = {
        aircraft: []
    }

    componentDidMount() {
        this.refreshList()
    }

    componentDidUpdate = (prevProps, prevState, snapshot) => {
        if (prevProps.update_id !== this.props.update_id) {
            this.refreshList()
        }
    }

    refreshList = () => {
        axios.get(`api/aircraft`)
            .then(res => {
                const aircraft = res.data;
                this.setState({ aircraft });
            })
    }


    render() {
        return (
            <table className="table table-striped table-bordered">
                <thead>
                <tr>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Health</th>
                    <th>Options</th>
                </tr>
                </thead>
                <tbody>
                { this.state.aircraft.map(item =>
                    <tr key={item.id}>
                        <td>{item.id}</td>
                        <td>{item.name}</td>
                        <td>{item.health}</td>
                        <td><button onClick={() => this.props.onSelect(item.id)}>View Maintenance History</button></td>
                    </tr>)
                }
                </tbody>
            </table>
        )
    }
}

