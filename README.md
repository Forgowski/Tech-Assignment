
# 📍 Tech-Assignment

A simple Django REST API for receiving and managing GPS location data.

## ✅ Requirements

To run this project, make sure you have the following Python packages installed:

- `Django`
- `djangorestframework`

You can install them using pip:

```bash
pip install django djangorestframework
```

---

## 🚀 Future Improvements

If given more time, I would definitely consider implementing the following enhancements:

- 🔐 **Authentication** – Secure the API so that only authorized devices or users can send location data.
- 🧪 **Unit Tests** – Ensure the stability and correctness of the system with automated test coverage.
- 🧹 **Better Validation** – Improve input validation to ensure data integrity and avoid unexpected errors.

---

## ❓ How Would You Prevent Location Spam?

One effective strategy to mitigate location spam is implementing a **rate limiter**.

> Each GPS device typically has its own IP address, so it's feasible to limit how many requests can be sent from a given IP over a certain period of time. This would help ensure fair use and prevent abuse of the system.

