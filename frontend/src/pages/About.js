import { Container, Header, Grid } from "semantic-ui-react";
import { Headline } from "../components/Headline";
import { MainMenu } from "../components/MainMenu";

export const About = () => {
  return (
    <Container style={{ marginTop: "4em" }} text textAlign="center">
      <Grid>
        <Grid.Row columns={1}>
          <Grid.Column>
            <Headline />
          </Grid.Column>
        </Grid.Row>

        <Grid.Row columns={1}>
          <Grid.Column>
            <MainMenu logo={false} />
          </Grid.Column>
        </Grid.Row>

        <Grid.Row columns={1}>
          <Grid.Column>
            <Container textAlign="left">
              <Header size="medium" content="What is Comprendo?" />
              <p>
                Comprendo is a Machine Learning tool that uses{" "}
                <a href="https://en.wikipedia.org/wiki/Named-entity_recognition">
                  Entity Extraction
                </a>{" "}
                to find interesting things on Twitter.
              </p>
              <Header size="medium" content="How does it work?" />
              <p>
                Comprendo combines a couple of cool cloud technologies to
                deliver interesting results. The core of Comprendo is{" "}
                <a href="https://aws.amazon.com/comprehend/">AWS Comprehend</a>{" "}
                - an AWS service that lets you use packaged machine models to
                pull out entities from text.
              </p>
              <p>
                When you enter a topic into Comprendo, it does a few things.
                First, it uses the{" "}
                <a href="https://developer.twitter.com/en/docs">Twitter API</a>{" "}
                to search Twitter for a bunch of tweets related to that topic.
                Then, it runs each of those tweets through AWS Comprehend to
                pull out all the entities it can. Finally, it filters the
                results and displays them.
              </p>
              <Header size="medium" content="Got questions?" />
              <p>
                This was a fun hobby project! Feel free to reach out to me on
                {" "}<a href="https://www.linkedin.com/in/zacharyjklein/">
                  LinkedIn
                </a>{" "}
                or check out {" "}<a href="https://zacharyjklein.com/">{" "}my website</a>{" "}
                if you want to know more!
              </p>
            </Container>
          </Grid.Column>
        </Grid.Row>
      </Grid>
    </Container>
  );
};
