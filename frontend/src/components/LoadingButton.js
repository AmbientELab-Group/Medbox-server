import React from "react";
import styled from "styled-components";
import CircularProgress from "@material-ui/core/CircularProgress";
import PrimaryButton from "./PrimaryButton";

const Wrapper = styled.div`
    position: relative;
`;

const ButtonProgress = styled(CircularProgress)`
    position: absolute;
    top: calc(50% - 12px);
    left: calc(50% - 12px);
`;

const LoadingButton = ({ children, isLoading, ...rest }) => {
    return (
        <Wrapper>
            <PrimaryButton disabled={isLoading} {...rest}>{children}</PrimaryButton>
            {isLoading && <ButtonProgress color="secondary" size={24} />}
        </Wrapper>
    );
};

export default LoadingButton;
