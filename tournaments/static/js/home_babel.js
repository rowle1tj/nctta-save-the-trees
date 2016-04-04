var data = [
    {
        itemText: 'Fill out Roster - CMU A vs MSU A',
        leftTeamName: 'CMU A',
        rightTeamName: 'MSU A',
        players: [
            'D1 - Li, Wei',
            'D2 - Huang, Hanye',
            'D3 - Emborsky, Eric',
            'D4 - Cvetkovski, Steven',
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
    },
    render: function() {
        return (
            <a href="#!" className="collection-item roster-fill-in" onClick={this.handleClick}>
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

ReactDOM.render(
    <ActionItemsList data={data} />, 
    document.getElementById('action-items')
);
