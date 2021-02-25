import { Container, Grid, Header } from "semantic-ui-react";
import { Headline } from "../components/Headline";
import { MainMenu } from "../components/MainMenu";
import { TopicSearch } from "../components/TopicSearch";

export const Home = () => {
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
            <Header size="small" content="What would you like to explore?" />
            <TopicSearch button />
          </Grid.Column>
        </Grid.Row>
      </Grid>
    </Container>
  );
};
