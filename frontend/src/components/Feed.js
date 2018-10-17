import React from "react";
import { render } from "react-dom";
import InfiniteScroll from "react-infinite-scroll-component";
import key from "weak-key";
import { fetchItems } from '../actions/feedActions';
import { connect } from 'react-redux';

class Feed extends React.Component {
  constructor(props) { 
    super(props)
  }

  fetchMoreData = () => {
    const oldData = this.props.items
    console.log('doing the fetch')
    this.props.fetchItems(oldData);
  };

  componentDidMount() {
    console.log('mounting feed');
    const oldData = this.props.items
    this.props.fetchItems(oldData);
  }

  render() {
    console.log('i am rendering');
    console.log(this.props.items)
    return (
      <div className="feed-section column is-two-thirds is-offset-2">
        <h1><center><div className="notfication feed-title">Passe Feed: Infinite Scroll of Remembrances</div></center></h1>
        <hr />
        <InfiniteScroll
          dataLength={this.props.items.length}
          next={this.fetchMoreData}
          hasMore={true}
          loader={<h4>Loading...</h4>}
        >
          {this.props.items.map((i, index) => (
            <div className="feed-item box" key={key(i)}>
            <div className="content feed-content">
           { i.item_parts.map(e => <p>{e.part}</p>) }
            </div>
            </div>
          ))}
        </InfiniteScroll>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  items: state.feed.items,
});

export default connect(mapStateToProps, { fetchItems })(Feed);

