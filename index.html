<!DOCTYPE html>
<html>
<head>
    <title>Auto Like Warpcast</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="text"], input[type="number"] {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        #status {
            margin-top: 10px;
            padding: 10px;
            border-radius: 4px;
        }
        .success {
            background-color: #d4edda;
            color: #155724;
        }
        .error {
            background-color: #f8d7da;
            color: #721c24;
        }
    </style>
    <script>
        function autoLike() {
            var authCode = document.getElementById("authCode").value;
            var targetUrl = document.getElementById("targetUrl").value;
            var likeInterval = document.getElementById("likeInterval").value;

            // Memastikan kedua field diisi
            if (authCode === "" || targetUrl === "") {
                setStatus("Silakan masukkan Authorization Code dan Target URL!", 'error');
                return;
            }

            // Mulai auto-like
            var intervalId = setInterval(function() {
                // Kirim request like ke Warpcast menggunakan fetch
                fetch("https://client.warpcast.com/v2/cast-likes", {
                    method: "PUT",
                    headers: {
                        "accept": "*/*",
                        "accept-language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",
                        "authorization": "Bearer " + authCode,
                        "content-type": "application/json; charset=utf-8",
                        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "\"Linux\"",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-site"
                    },
                    referrer: "https://warpcast.com/",
                    referrerPolicy: "strict-origin-when-cross-origin",
                    body: JSON.stringify({ castHash: targetUrl }),
                    mode: "cors",
                    credentials: "include"
                })
                .then(response => {
                    if (response.ok) {
                        setStatus("Like berhasil dikirim ke " + targetUrl, 'success');
                    } else {
                        setStatus("Gagal mengirim like ke " + targetUrl, 'error');
                    }
                })
                .catch(error => {
                    setStatus("Gagal mengirim like ke " + targetUrl + ": " + error, 'error');
                });

                // Menghentikan auto-like setelah selesai
                clearInterval(intervalId);
            }, likeInterval * 1000); // Konversi jeda per like ke milidetik
        }

        function setStatus(message, status) {
            var statusDiv = document.getElementById("status");
            statusDiv.innerText = message;
            statusDiv.className = status;
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>Auto Like Warpcast</h1>
        <label for="authCode">Authorization Code:</label>
        <input type="text" id="authCode">
        <label for="targetUrl">Target URL:</label>
        <input type="text" id="targetUrl">
        <label for="likeInterval">Jeda per Like (detik):</label>
        <input type="number" id="likeInterval" value="10">
        <button onclick="autoLike()">Mulai Auto Like</button>
        <div id="status"></div>
    </div>
</body>
</html>
