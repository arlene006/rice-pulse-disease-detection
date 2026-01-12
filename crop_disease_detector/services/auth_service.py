from abc import ABC, abstractmethod
import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
from typing import Optional

class IAuthService(ABC):
    """
    Interface for Authentication Service.
    Follows DIP: The app depends on this interface, not the concrete implementation.
    """
    @abstractmethod
    def login(self) -> bool:
        """Displays login UI and returns True if logged in."""
        pass

    @abstractmethod
    def get_username(self) -> Optional[str]:
        """Returns the current username."""
        pass
    
    @abstractmethod
    def logout(self):
        """Logs out the user."""
        pass

class StreamlitAuthService(IAuthService):
    """
    Concrete implementation of AuthService using streamlit_login_auth_ui.
    Encapsulates the 3rd party library dependency.
    """
    def __init__(self):
        self._login_obj = None
        self._username = None
        self._is_logged_in = False

    def _init_login_widget(self):
        if self._login_obj is None:
            self._login_obj = __login__(
                auth_token="courier_auth_token",
                company_name="Shims",
                width=200,
                height=250,
                logout_button_name='Logout',
                hide_menu_bool=False,
                hide_footer_bool=False,
                lottie_url='https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json'
            )

    def login(self) -> bool:
        try:
            self._init_login_widget()
            self._is_logged_in = self._login_obj.build_login_ui()
            
            if self._is_logged_in:
                self._username = self._login_obj.get_username()
                
            return self._is_logged_in
        except Exception as e:
            st.error(f"Auth specific error: {str(e)}")
            return False

    def get_username(self) -> Optional[str]:
        return self._username

    def logout(self):
        # The library handles logout via its own UI button usually,
        # but if we needed programmatic logout, we'd add it here.
        pass
