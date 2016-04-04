var data = [
    {
        itemText: 'Fill out Roster - CMU A vs MSU A',
        leftTeamName: 'CMU A',
        rightTeamName: 'MSU A',
        players: [
            'D1 - Li, Wei',
            'D2 - Huang, Hanye',
            'D3 - Emborsky, Eric',
            'D4 - Cvetkovski, Steven'
        ],
        opponents: [
            '(1894) Lu, Xiaotian',
            '(572) Sang, Yifan',
            '(1586) Lu, Yiqiao'
        ]
    },
    {itemText: 'Item 2'},
    {itemText: 'Item 3'}
];  

var ActionItem = React.createClass({
    handleClick: function(event) {
        console.log(this.props.roster_data);
        ReactDOM.render(
            <RosterModal roster={this.props.roster_data}/>, 
            document.getElementById('modal-container')
        );
        $('#modal1').openModal();
        $('ul.tabs').tabs();
        $('select').material_select();
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
    render: function() {
        var listItems = this.props.data.map(function(listItem, i) {
            return (
                <ActionItem roster_data={listItem} key={i}></ActionItem>
            );
        });

        return (
            <div>
            <h3>Action Items</h3>
            <div className="collection">
                {listItems} 
            </div>
            </div>
        );
    }
}); 


var RosterModal = React.createClass({
    render: function() {
        var opponents = this.props.roster.opponents.map(function(opponent, i) {
            return (
                <li className="collection-item">{opponent}</li>
            );
        });

        var players = this.props.roster.players.map(function(player, i) {
            return (
                <a href="#!" className="collection-item">{player}<span className="badge">{i+1}</span></a>
            );
        });

        var playerOptions = this.props.roster.players.map(function(player, i) {
            if (i > 0) {
                return (
                    <option value="{i+1}">{player}</option>
                );
            }
        });
        
        return (
            <div id="modal1" className="modal modal-fixed-footer">
                <div className="modal-content">
                    <div className="row center-align valign-wrapper">
                        <div className="col l5 s5"><h5>{this.props.roster.leftTeamName}</h5></div>
                        <div className="col l2 s2 valign">vs.</div>
                        <div className="col l5 s5"><h5>{this.props.roster.rightTeamName}</h5></div>
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
                                <li className="collection-item">D1 - Li, Wei</li>
                                <li className="collection-item">
                                    <select value="1">
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

