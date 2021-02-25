import { Card, Container, Feed, Header, Icon, List } from "semantic-ui-react";

String.prototype.toTitleCase = function () {
  return this.replace(/\w\S*/g, function (txt) {
    return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
  });
};

const icons = {
  Organization: "handshake",
  Person: "user",
  Location: "globe",
  Title: "font",
  Quantity: "numbered list",
  Date: "calendar",
  Other: "list",
};

export const FetchedTopics = (props) => {
  if (Object.entries(props.results.body.result).length === 0)
    return <p>No results!</p>;
  let items = [];
  Object.entries(props.results.body.result).map((entry) => {
    let feed = [];
    Object.entries(entry[1]).map((subitem) => {
      feed.push(
        <List.Item>
          <List.Content>
            <Header size="small">
              <a href={`https://www.google.com/search?q=${subitem[1].text}`}>{subitem[1].text}</a>
            </Header>
            <List.Description>
              {`Average score: ${subitem[1].avg_score}%`}
            </List.Description>
            <List.Description>
              {`Occurrences: ${subitem[1].occurrences}`}
            </List.Description>
          </List.Content>
        </List.Item>
      );
    });

    items.push(
      <>
        <List.Item>
          <List.Icon name={icons[entry[0].toTitleCase()]} />
          <List.Content>
          <Header size="medium">{entry[0].toTitleCase()}</Header>
          </List.Content>
        </List.Item>
        <List.Item>
          <List.List>{feed}</List.List>
        </List.Item>
      </>
    );
  });
  return <List divided>{items}</List>;
};

export const ErrorGettingTopic = (props) => {
  return (
    <Container text>
      <Header icon>
        <Icon name="warning sign" color="yellow" />
        <Header size="medium" content="Oh no! Something broke." />
      </Header>
      <p>
        <code>{props.results.body.result}</code>
      </p>
      <p>It's not you, it's us. Please try again later!</p>
    </Container>
  );
};

export const Topics = (props) => {
  return (
    <>
      {!props.results.body.error ? (
        <FetchedTopics {...props} />
      ) : (
        <ErrorGettingTopic {...props} />
      )}
    </>
  );
};

export const TopicCards = (props) => {
  return <>{props.results ? <Topics {...props} /> : <></>}</>;
};
