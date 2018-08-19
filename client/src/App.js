import React, {Component} from 'react';
import './App.css';
import AircraftList from './AircraftList'
import AircraftMaintenance from "./AircraftMaintenance";
import AddMaintenance from "./AddMaintenance";

class App extends Component {
    state = {
        aircraft_id: null,
        update_id: 0
    }

  render() {

        this.handleAircraftSelected = (aircraft_id) => {
          this.setState({aircraft_id})
      }

      const handleMaintenanceUpdate = () => {
            this.setState({update_id: this.state.update_id + 1})
      }

      return (
      <div className="App">
          <div>
              <h1>Aircraft Health</h1>
              <AircraftList onSelect={this.handleAircraftSelected} />
          </div>
          <hr/>
          <div>
              <h2>Maintenance History</h2>
              {this.state.aircraft_id ? <AircraftMaintenance update_id={this.state.update_id} aircraft_id={this.state.aircraft_id}/> : <span>Select an Aircraft to view history.</span>}
              <hr/>
              {this.state.aircraft_id ?
              <div>
                  <h3>Add Maintenance Record</h3>
                  <AddMaintenance aircraft_id={this.state.aircraft_id} onMaintenanceChange={handleMaintenanceUpdate} />
              </div> : null}
          </div>
      </div>
    );
  }

}

export default App;
