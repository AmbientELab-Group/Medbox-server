import React, { useState } from "react";
import MuiTextField from "@material-ui/core/TextField";
import InputAdornment from "@material-ui/core/InputAdornment";
import Visibility from "@material-ui/icons/Visibility";
import VisibilityOff from "@material-ui/icons/VisibilityOff";
import IconButton from "@material-ui/core/IconButton";
import { useTranslation } from "react-i18next";

const PasswordField = (props) => {
    const [isPasswordHidden, setPasswordHidden] = useState(true);
    const { t } = useTranslation("account");

    return (
        <MuiTextField
            {...props}
            variant="outlined"
            fullWidth
            type={isPasswordHidden ? "password" : "text"}
            InputProps={{
                endAdornment: (
                    <InputAdornment position="end">
                        <IconButton
                            aria-label={t("aria.passwordVisibilityToggle")}
                            onClick={() => setPasswordHidden(!isPasswordHidden)}
                            onMouseDown={(e) => e.preventDefault()}
                        >
                            {isPasswordHidden ? (
                                <Visibility />
                            ) : (
                                <VisibilityOff />
                            )}
                        </IconButton>
                    </InputAdornment>
                ),
            }}
        />
    );
};

export default PasswordField;
