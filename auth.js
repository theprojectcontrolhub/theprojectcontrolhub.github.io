// Firebase Configuration - The Project Control Hub
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import {
  getAuth,
  GoogleAuthProvider,
  signInWithPopup,
  signInWithRedirect,
  getRedirectResult,
  signOut,
  onAuthStateChanged
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
// Always prompt account selection (nicer UX, avoids silent-fail on some devices)
provider.setCustomParameters({ prompt: "select_account" });

// Detect mobile / in-app browsers where popups fail
function isMobile() {
  return /Android|iPhone|iPad|iPod|Mobile|webOS|BlackBerry|IEMobile|Opera Mini/i.test(
    navigator.userAgent
  );
}

// On page load, complete any pending redirect sign-in.
// This runs automatically when the user comes back from the Google redirect.
getRedirectResult(auth).catch((error) => {
  // Non-fatal: just log. The auth state listener will handle the result.
  console.error("Redirect result error:", error);
});

// Sign in — popup on desktop, redirect on mobile
export async function signInWithGoogle() {
  if (isMobile()) {
    // Redirect flow: navigates away to Google, then back to the site.
    // No return value here — onUserChange fires after redirect completes.
    await signInWithRedirect(auth, provider);
    return null;
  }

  // Desktop: popup flow. If the popup is blocked, fall back to redirect.
  try {
    const result = await signInWithPopup(auth, provider);
    return result.user;
  } catch (error) {
    const code = error && error.code ? error.code : "";
    if (
      code === "auth/popup-blocked" ||
      code === "auth/popup-closed-by-user" ||
      code === "auth/cancelled-popup-request" ||
      code === "auth/operation-not-supported-in-this-environment"
    ) {
      // Popup didn't work — use redirect instead
      await signInWithRedirect(auth, provider);
      return null;
    }
    console.error("Giriş hatası:", error);
    throw error;
  }
}

// Sign out
export async function logout() {
  try {
    await signOut(auth);
  } catch (error) {
    console.error("Çıkış hatası:", error);
  }
}

// Watch auth state
export function onUserChange(callback) {
  return onAuthStateChanged(auth, callback);
}
