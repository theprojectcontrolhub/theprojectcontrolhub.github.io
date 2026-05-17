// Firebase Configuration - The Project Control Hub
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut, onAuthStateChanged } 
  from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";

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

// Giriş yap
export async function signInWithGoogle() {
  try {
    const result = await signInWithPopup(auth, provider);
    return result.user;
  } catch (error) {
    console.error("Giriş hatası:", error);
    throw error;
  }
}

// Çıkış yap
export async function logout() {
  try {
    await signOut(auth);
  } catch (error) {
    console.error("Çıkış hatası:", error);
  }
}

// Kullanıcı durumunu izle
export function onUserChange(callback) {
  return onAuthStateChanged(auth, callback);
}
