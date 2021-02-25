import { Container, Grid } from "semantic-ui-react";
import { Headline } from "../components/Headline";
import { MainMenu } from "../components/MainMenu";
import { TopicSearch } from "../components/TopicSearch";
import { TopicService } from "../apis/index.js";

import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import { TopicCards } from "../components/TopicCards";

function useQuery() {
  return new URLSearchParams(useLocation().search);
}

export const Results = () => {
  let query = useQuery();
  const [loading, setLoading] = useState(true);
  const [results, setResults] = useState(null);

  useEffect(() => {
    let getResults = async () => {
      let response = await TopicService.fetchTopic(query.get("q"));
      setResults(response.data);
      setLoading(false);
    };
    getResults();
  }, []);
  return (
    <Container style={{ marginTop: "4em" }}>
      <Grid>
        <Grid.Row columns={1}>
          <Grid.Column width={2}>
            <Headline />
          </Grid.Column>
        </Grid.Row>

        <Grid.Row columns={1}>
          <Grid.Column>
            <MainMenu />
          </Grid.Column>
        </Grid.Row>

        <Grid.Row columns={1}>
          <Grid.Column>
            <TopicSearch maxWidth="50%" loading={loading} initial={query.get("q")} />
          </Grid.Column>
        </Grid.Row>

        <Grid.Row columns={1}>
          <Grid.Column>
            <TopicCards results={results} />
          </Grid.Column>
        </Grid.Row>
      </Grid>
    </Container>
  );
};
