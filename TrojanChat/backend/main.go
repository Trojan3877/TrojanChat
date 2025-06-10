// main.go
//
// Service: TrojanChat Messaging Microservice
// Author: Corey Leath
//
// A lightweight Go HTTP server providing REST endpoints for message send/receive.
// Uses Gorilla Mux router and communicates with Firebase via the Firebase Admin SDK.

package main

import (
    "context"
    "encoding/json"
    "log"
    "net/http"
    "os"
    "time"

    "github.com/gorilla/mux"
    firebase "firebase.google.com/go"
    "google.golang.org/api/option"
)

type Message struct {
    UserID  string `json:"userId"`
    Text    string `json:"text"`
    Created int64  `json:"created"`
}

var fbApp *firebase.App

func initFirebase() {
    ctx := context.Background()
    saKey := os.Getenv("FIREBASE_SERVICE_ACCOUNT")
    opt := option.WithCredentialsFile(saKey)
    app, err := firebase.NewApp(ctx, nil, opt)
    if err != nil {
        log.Fatalf("error initializing firebase app: %v", err)
    }
    fbApp = app
}

func sendMessage(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()
    var msg Message
    if err := json.NewDecoder(r.Body).Decode(&msg); err != nil {
        http.Error(w, "invalid payload", http.StatusBadRequest)
        return
    }
    msg.Created = time.Now().Unix()
    // Write to Firestore
    client, err := fbApp.Firestore(ctx)
    if err != nil {
        http.Error(w, "firestore init error", http.StatusInternalServerError)
        return
    }
    defer client.Close()
    _, _, err = client.Collection("messages").Add(ctx, msg)
    if err != nil {
        http.Error(w, "failed to save message", http.StatusInternalServerError)
        return
    }
    w.WriteHeader(http.StatusCreated)
    json.NewEncoder(w).Encode(msg)
}

func getMessages(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()
    client, err := fbApp.Firestore(ctx)
    if err != nil {
        http.Error(w, "firestore init error", http.StatusInternalServerError)
        return
    }
    defer client.Close()
    iter := client.Collection("messages").OrderBy("created", firebase.Desc).Documents(ctx)
    var msgs []Message
    for {
        doc, err := iter.Next()
        if err != nil {
            break
        }
        var m Message
        doc.DataTo(&m)
        msgs = append(msgs, m)
    }
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(msgs)
}

func main() {
    initFirebase()
    r := mux.NewRouter()
    r.HandleFunc("/messages", sendMessage).Methods("POST")
    r.HandleFunc("/messages", getMessages).Methods("GET")
    addr := ":8080"
    log.Printf("TrojanChat microservice listening on %s", addr)
    log.Fatal(http.ListenAndServe(addr, r))
}


mkdir -p TrojanChat/backend
git add TrojanChat/backend/main.go
git commit -m "Add Go microservice for message handling"
git push
