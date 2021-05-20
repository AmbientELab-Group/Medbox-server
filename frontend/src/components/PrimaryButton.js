import Button from "@material-ui/core/Button";
import styled from "styled-components";

const PrimaryButton = styled(Button)`
    background: ${({ theme }) => theme.palette.primary.gradient};
    font-weight: 600;
    border: 0;
    box-shadow: 0 3px 5px 2px rgba(255, 105, 135, 0.3);
    color: white;
    padding: 1em 2em;
`;

export default PrimaryButton;
