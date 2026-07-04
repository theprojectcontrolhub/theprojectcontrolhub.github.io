// Firebase Configuration - The Project Control Hub
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import {
  getAuth,
  GoogleAuthProvider,
  signInWithPopup,
  signInWithRedirect,
  getRedirectResult,
  signOut,
  onAuthStateChanged,
  browserPopupRedirectResolver
} from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyA7BepKxVlP2DEHD7HI0cWx3viiAqpxfTM",
  authDomain: "theprojectcontrolhub.firebaseapp.com",
  projectId: "theprojectcontrolhub",
  storageBucket: "theprojectcontrolhub.firebasestorage.app",
  messagingSenderId: "803522502727",
  appId: "1:803522502727:web:842858067d87eeb1a3d162",
  measurementId: "G-50Z3CT30FG"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();
provider.setCustomParameters({ prompt: "select_account" });

// Complete any pending redirect result on load (fallback path only).
getRedirectResult(auth).catch((error) => {
  console.error("Redirect result error:", error);
});

// Sign in with Google.
// POPUP first on every device — modern mobile browsers support it and it avoids
// the third-party-cookie failures that break signInWithRedirect. Redirect only
// as a last resort when the popup genuinely cannot run.
export async function signInWithGoogle() {
  try {
    const result = await signInWithPopup(auth, provider, browserPopupRedirectResolver);
    return result.user;
  } catch (error) {
    const code = (error && error.code) ? error.code : "";

    if (
      code === "auth/popup-closed-by-user" ||
      code === "auth/cancelled-popup-request"
    ) {
      return null; // user dismissed — let them retry
    }

    if (
      code === "auth/popup-blocked" ||
      code === "auth/operation-not-supported-in-this-environment"
    ) {
      await signInWithRedirect(auth, provider); // fallback
      return null;
    }

    console.error("Giriş hatası:", error);
    throw error;
  }
}

export async function logout() {
  try {
    await signOut(auth);
  } catch (error) {
    console.error("Çıkış hatası:", error);
  }
}

export function onUserChange(callback) {
  return onAuthStateChanged(auth, callback);
}
