import React from 'react';
import {Button, ControlLabel, FormControl, FormGroup, HelpBlock, Radio} from 'react-bootstrap'
import axios from "axios/index";

function FieldGroup({ id, label, help, ...props }) {
    return (
        <FormGroup controlId={id}>
            <ControlLabel>{label}</ControlLabel>
            <FormControl {...props} />
            {help && <HelpBlock>{help}</HelpBlock>}
        </FormGroup>
    );
}
export default class AddMaintenance extends React.Component {

    state = {
        description: '',
        blocked: false
    }

    handleDescChange = (event) => {
        this.setState({description: event.target.value});
    }

    handleBlockedChange = (event) => {
        this.setState({blocked: event.target.value});
    }

    handleSubmit = (event) => {
        axios.post(`api/maintenance/${this.props.aircraft_id}`, {
            description: this.state.description,
            blocked: this.state.blocked === 'true'
        })
            .then(res => {
                this.setState({
                    description: '',
                    blocked: false
                });
                this.props.onMaintenanceChange()
                alert('submitted')
            })
        event.preventDefault()
    }

    render() {
        return (
        <form>
            <FieldGroup
                id="formControlsDescription"
                type="text"
                label="Maintenance Description"
                placeholder="Enter Description"
                value={this.state.description}
                onChange={this.handleDescChange}
            />
            <FormGroup onChange={this.handleBlockedChange}>
                <ControlLabel>Does maintenance block flight?</ControlLabel>
                <Radio value={true} checked={this.state.blocked} name="radioGroup" inline onChange={this.handleBlockedChange}>
                    Yes
                </Radio>
                <Radio value={false} checked={!this.state.blocked} name="radioGroup" inline onChange={this.handleBlockedChange}>
                    No
                </Radio>
            </FormGroup>
            <Button type="submit" onClick={this.handleSubmit}>Submit</Button>
        </form>
        )
    }
}