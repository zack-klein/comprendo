import { useState } from "react";
import { Redirect } from "react-router-dom";
import { Form } from "semantic-ui-react";

var faker = require("faker");

export const TopicSearch = (props) => {
  const [topic, setTopic] = useState(props.initial || "");
  const [redirect, setRedirect] = useState(null);
  if (redirect) return <Redirect to={redirect} />;
  return (
    <Form onSubmit={() => setRedirect(`/topic?q=${topic}`)}>
      <Form.Input
        placeholder={
          props.placeholder ||
          `${faker.name.findName()}`
        }
        onChange={(e) => setTopic(e.target.value)}
        value={topic}
        loading={props.loading || false}
        style={props.maxWidth ? { maxWidth: props.maxWidth } : {} }
      />
      {props.button ? (
        <Form.Button
          content="Submit"
          color="green"
          loading={props.loading || false}
          basic
        />
      ) : (
        <></>
      )}
    </Form>
  );
};
