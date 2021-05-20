import styled, { css } from "styled-components";
import Typography from "@material-ui/core/Typography";

const SubmitMessage = styled(Typography)`
    text-align: "center";
    display: none;

    ${({ $error }) =>
        $error &&
        css`
            color: ${({ theme }) => theme.palette.error.main};
            display: block;
        `};

    ${({ $success }) =>
        $success &&
        css`
            color: ${({ theme }) => theme.palette.success.main};
            display: block;
        `};
`;

export default SubmitMessage;
