
//let bookslist_url = JSON.parse(document.getElementById("booklist-data").textContent)/
//window.location.pathname = book_data_url


class BookDisplay extends React.Component {
    constructor(props) {
        super(props);

        this.state = {

            books: [],
            url: 'http://127.0.0.1:8000/api/books',
            fetchInProgress: false,
        };
    }

    doFetch() {
        if (this.state.fetchInProgress)
            return;

        this.setState({
            fetchInProgress: true
        })

        fetch(this.state.url, {
            method: 'GET',
            headers: {
                Accept: 'application/json'
            }
        }).then((response) => {
            return response.json();
        }).then((data) => {
            this.setState({
                fetchInProgress: false, books: data
            })
        })
    }

    render() {
        const bookListItems = this.state.books.map((book) => {
            return <li key={book.pk}>{book.title}</li>;
        })

        const buttonText = this.state.fetchInProgress ?
            'Fetch in Progress' : 'Fetch';

        return <div>
            <ul>{bookListItems}</ul>
            <button onClick={() => this.doFetch()} disabled={this.state.fetchInProgress}>
                {buttonText}
            </button>
        </div>
    }
}

ReactDOM.render(
    <BookDisplay />, document.getElementById('react_container')
);




// const e = React.createElement;
/* let users_name = JSON.parse(document.getElementById("username").textContent)
let target_value = JSON.parse(document.getElementById("target-value").textContent)

class ClickCounter extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            clickCount: 0,
        }
    }
    render() {
        if (this.state.clickCount === parseInt(target_value)) {
            return <span>Well done, {users_name}</span>
        }

        //using JSX instead of react.createElement
        return (
            <button
                onClick={
                    () => this.setState({
                        clickCount: this.state.clickCount + 1
                    })
                }>
                {this.state.clickCount}
            </button>
        )

        e(
            'button',
            {
                onClick: () => this.setState({
                    clickCount: this.state.clickCount + 1
                })
            },
            this.state.clickCount
        );
    }
}

ReactDOM.render(
    <ClickCounter />, document.getElementById('react_container')
); */
