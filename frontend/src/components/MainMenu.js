import { Button, Image } from "semantic-ui-react";
import {Link} from "react-router-dom";

export const MainMenu = () => (
    <Button.Group>
        <Button as={Link} to="/" content="Home" basic />
        <Button as={Link} to="/about" content="About" basic />
    </Button.Group>
)