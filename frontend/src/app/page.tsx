"use client";

import { useState } from "react";
import Image from "next/image";
import { Upload } from "lucide-react";
import api from "@/services/api";
import { toast } from "sonner";

type Source = {
  source: string;
  page: number;
};

type Message = {
  role: "user" | "ai";
  text: string;
  sources?: Source[];
};

export default function Home() {
  const [document, setDocument] = useState<File | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [uploading, setUploading] = useState(false);
  const [chatLoading, setChatLoading] = useState(false);

  const handleUpload = async (file: File) => {
    if (!file) {
      toast.warning("Please select a file first");
      return;
    }

    const toastId = toast.loading("Uploading document...");

    try {
      setUploading(true);

      const formData = new FormData();
      formData.append("pdf_file", file);

      const response = await api.post("/upload-pdf", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      console.log(response.data);
      if (!response.data.success) {
        throw new Error(response.data.error);
      }

      setDocument(file);

      toast.success("Document uploaded successfully!", {
        id: toastId,
      });

      setMessages([
        {
          role: "ai",
          text: `Great! I've loaded "${file.name}". I'm ready to answer questions about this document.`,
        },
      ]);
    } catch (error) {
      console.error(error);
      toast.error("Upload failed", {
        id: toastId,
      });
    } finally {
      setUploading(false);
    }
  };

  const handleSend = async () => {
    console.log("HANDLE SEND CALLED");

    if (!input.trim()) return;
    console.log(input);

    const userMessage: Message = {
      role: "user",
      text: input,
    };

    setMessages((prev) => [...prev, userMessage]);
    console.log(messages);

    const currentQuestion = input;
    console.log(currentQuestion);

    setInput("");

    try {
      setChatLoading(true);
      const response = await api.post("/ask-questions", {
        query: currentQuestion,
      });

      console.log("Ask Question Response:", response.data);

      if (!response.data.success) {
        throw new Error(response.data.error);
      }

      const aiMessage: Message = {
        role: "ai",
        text: response.data.result,
        sources: response.data.sources,
      };

      console.log(aiMessage);
      setMessages((prev) => [...prev, aiMessage]);
    } catch (err: unknown) {
      toast.error("Failed to get AI response");
      console.error(err);

      setMessages((prev) => [
    ...prev,
    {
      role: "ai",
      text:
        "I've temporarily reached my AI usage limit and can't process more questions right now. Please wait a moment and try again. Your document is still loaded and ready for use."
    },
  ]);
    } finally {
      setChatLoading(false);
    }
  };

  const handleNewDocument = async () => {
    setDocument(null);
    setMessages([]);
    setInput("");
  };

  return (
    <main className="flex h-screen bg-gray-100 font-sans">
      <section className="w-1/4 bg-white border-gray-200 border-r p-8 flex flex-col h-screen">
        <div>
          <div className="flex gap-4">
            <Image src="/logo.png" width={50} height={30} alt="logo" />
            <div className="flex flex-col">
              <h1 className="text-2xl font-bold">DocDoctor AI</h1>
              <p className="text-sm text-gray-600">Chat with your docs</p>
            </div>
          </div>

          <hr className="my-6 border-gray-200" />
        </div>

        <div className="flex-1">
          <div className="mt-4">
            {!document ? (
              <div className="border border-gray-300 rounded-xl p-3 bg-gray-50">
                <div className="flex items-center gap-2 mb-2">
                  <Upload size={18} className="text-gray-500" />
                  <h3 className="font-medium">Document</h3>
                </div>
                <p className="text-gray-600 text-sm">
                  No document uploaded yet
                </p>
              </div>
            ) : (
              <div>
                <button
                  onClick={handleNewDocument}
                  className="w-full bg-violet-500 hover:bg-violet-600 text-white rounded-xl py-3 px-4 font-medium transition cursor-pointer"
                >
                  + Upload New Document
                </button>
                <hr className="my-2 border-gray-50" />
                <div className="border border-violet-200 bg-violet-50 rounded-xl p-3">
                  <h3 className="font-medium text-violet-800">
                    {document.name}
                  </h3>
                  <p className="text-xs text-violet-600 mt-1">Ready to chat</p>
                </div>
              </div>
            )}
          </div>
        </div>

        <div className="text-sm text-gray-600">
          <hr className="my-4 border-gray-200" />
          Powered by AI • Secure & Private
        </div>
      </section>

      <section className="w-3/4 bg-white">
        {!document ? (
          <div className="h-full flex flex-col justify-center items-center">
            <Image src="/logo.png" width={70} height={70} alt="logo" />
            <h1 className="text-2xl font-bold mt-4 mb-2">
              Welcome to DocDoctor AI
            </h1>
            <p className="text-gray-600 text-md">
              Upload a PDF document to start chatting with your content
            </p>
            <div className="mt-8 w-full max-w-2xl">
              <label className="border-2 border-dashed border-gray-300 bg-gray-50 rounded-2xl p-12 flex flex-col items-center justify-center cursor-pointer hover:bg-gray-100 transition">
                <Upload size={45} className="text-gray-500 mb-4" />

                <p className="text-gray-700 text-md font-semibold">
                  Drop your PDF here or click to browse
                </p>

                <p className="text-sm text-gray-600 mt-2">
                  Supports PDF files up to 50MB
                </p>

                <input
                  type="file"
                  accept="application/pdf"
                  className="hidden"
                  disabled={uploading}
                  onChange={(e) => {
                    const file = e.target.files?.[0];
                    if (file) handleUpload(file);
                  }}
                />
              </label>

              <div className="mt-6 gap-10 flex space-y-8">
                <div className="border border-gray-50 w-50 rounded-xl p-4 bg-gray-50 h-20">
                  <h4 className="font-bold text-md ">Instant Answers</h4>
                  <p className="text-xs text-gray-600 mt-1">
                    Get AI-powered responses
                  </p>
                </div>

                <div className="border border-gray-50 w-50 rounded-xl p-4 bg-gray-50 h-20">
                  <h4 className="font-bold text-md">Private & Secure</h4>
                  <p className="text-xs text-gray-600 mt-1">
                    Your data stays protected
                  </p>
                </div>

                <div className="border border-gray-50 w-50 rounded-xl p-4 bg-gray-50 h-20">
                  <h4 className="font-bold text-md">Smart Search</h4>
                  <p className="text-xs text-gray-600 mt-1">
                    Find info quickly
                  </p>
                </div>
              </div>
            </div>
          </div>
        ) : (
          <div className="h-full flex flex-col">
            <div className="border-b border-gray-200 p-4">
              <h2 className="font-semibold text-lg">{document?.name}</h2>

              <p className="text-sm text-gray-500">
                Ask questions about your document
              </p>
            </div>

            <div className="flex-1 overflow-y-auto p-6 space-y-4">
              {messages.length === 0 && (
                <div className="text-center text-gray-500 mt-50">
                  Start the conversation by asking a question
                </div>
              )}

              {messages.map((msg, index) => (
                <div
                  key={index}
                  className={`flex ${
                    msg.role === "user" ? "justify-end" : "justify-start"
                  }`}
                >
                  <div
                    className={`max-w-xl px-4 py-3 rounded-2xl text-sm ${
                      msg.role === "user"
                        ? "bg-violet-500 text-white"
                        : "bg-gray-100 text-gray-800"
                    }`}
                  >
                    <p>{msg.text}</p>

                    {msg.role === "ai" &&
                      msg.sources &&
                      msg.sources.length > 0 && (
                        <div className="mt-3 pt-3 border-t border-gray-300">
                          <p className="text-xs font-semibold text-gray-500 mb-1">
                            Sources
                          </p>

                          {msg.sources.map((source, idx) => (
                            <div key={idx} className="text-xs text-gray-500">
                              📄 {source.source} • Page {source.page}
                            </div>
                          ))}
                        </div>
                      )}
                  </div>
                </div>
              ))}

              {chatLoading && (
                <div className="text-sm text-gray-500">AI is thinking...</div>
              )}
            </div>

            <div className="border-t border-gray-200 p-4 flex gap-3">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask something about your PDF..."
                className="flex-1 border border-gray-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-violet-500"
              />

              <button
                onClick={handleSend}
                disabled={chatLoading}
                className="bg-violet-500 hover:bg-violet-600 cursor-pointer text-white px-6 rounded-xl transition"
              >
                {chatLoading ? "Thinking..." : "Send"}
              </button>
            </div>
          </div>
        )}
      </section>
    </main>
  );
}
