var ActionItem = React.createClass({
    handleClick: function(event) {
        this.props.itemClick(this.props.roster_data);
    },
    render: function() {
        return (
            <a href="#!" className="collection-item rooster-fill-in" onClick={this.handleClick}>
                {this.props.roster_data.itemText}
                <i className="secondary-content mdi-content-send"></i>
            </a>
        );
    }
}); 

var ActionItemsList = React.createClass({
    getInitialState: function() {
        return {
            roster_data: {
                players: [],
                opponents: [],
                numPlayersClicked: 0,
                leftTeamName: '',
                rightTeamName: ''
            }
        }
    },
    itemClick: function(roster) {
        this.setState({roster_data: roster});

        $('#modal1').openModal();
        $('ul.tabs').tabs();
    },
    render: function() {
        var itemClick = this.itemClick;
        var listItems = this.props.data.map(function(listItem, i) {
            return (
                <ActionItem roster_data={listItem} key={i} itemClick={itemClick}></ActionItem>
            );
        });

        return (
            <div>
            <h3>Action Items</h3>
            <div className="collection">
                {listItems} 
            </div>
            <RosterModal data={this.state.roster_data} />
            </div>
        );
    }
});

var RosterPlayerItem = React.createClass({
    getInitialState: function() {
        return {active: false}
    },
    handleClick: function(event) {
        this.props.onClick(event, this);
    },

    render: function() {
        return (
            <a href="#!" className="collection-item" key={this.props.number+1} onClick={this.handleClick}>
                {this.props.player} <span className="badge">{this.props.number+1}</span>
            </a>
        );
    }
});


var RosterModal = React.createClass({
    getInitialState: function() {
        return {
            players: [],
            opponents: [],
            numPlayersClicked: 0,
            leftTeamName: '',
            rightTeamName: ''
        };
    },

    playerClick: function(event, player) {
        if (this.state.numPlayersClicked < 4) {
            this.setState({numPlayersClicked: this.state.numPlayersClicked + 1});
        }
    },

    render: function() {
        var thisRosterModal = this;
        var opponents = this.props.data.opponents.map(function(opponent, i) {
            return (
                <li className="collection-item" key={i+1}>{opponent}</li>
            );
        });

        var players = this.props.data.players.map(function(player, i) {
            return (
                <RosterPlayerItem player={player} number={i} onClick={thisRosterModal.playerClick} key={player}/>
            );
        });

        var playerOptions = this.props.data.players.map(function(player, i) {
            if (i > 0) {
                return (
                    <option value="{i+1}" key={i+1}>{player}</option>
                );
            }
        });
        
        return (
            <div id="modal1" className="modal modal-fixed-footer">
                <div className="modal-content">
                    <div className="row center-align valign-wrapper">
                        <div className="col l5 s5"><h5>{this.props.data.leftTeamName}</h5></div>
                        <div className="col l2 s2 valign">vs.</div>
                        <div className="col l5 s5"><h5>{this.props.data.rightTeamName}</h5></div>
                    </div>
                    <div className="row">
                        <div className="col s12">
                            <ul className="tabs">
                                <li className="tab col s6"><a className="active" href="#roster-players-tab">Players</a></li>
                                <li className="tab col s6"><a href="#roster-opponents-tab">Opponents</a></li>
                            </ul>
                        </div>
                        <div id="roster-players-tab" className="col s12">
                            <div className="collection">
                                {players}
                            </div>

                            <h5>Doubles</h5>
                            <ul id="doubles-list" className="collection">
                                <li className="collection-item">{this.props.data.players[0]}</li>
                                <li className="collection-item">
                                    <select >
                                        <option value="" disabled>Select doubles partner</option>
                                        {playerOptions}
                                    </select>
                                </li>
                            </ul>
                        </div>
                        <div id="roster-opponents-tab" className="col s12">
                            <ul className="collection">
                                {opponents}
                            </ul>
                        </div>
                    </div>            
                </div>
                <div className="modal-footer">
                    <a href="#" className="waves-effect waves-green btn-flat modal-action modal-close">Submit Roster</a>
                </div>
            </div>
        );
    }
});

ReactDOM.render(
    <ActionItemsList data={data} />, 
    document.getElementById('action-items')
);

