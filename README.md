# Binomial-Options---Iterating-Over-Fidelity-Stock-Price-Volatility

# 📈 Binomial Options Pricing Models

This repository contains a set of Python scripts that model **European call and put options** using the **binomial options pricing model (BOPM)** framework. Each script explores how option values change relative to one of three key variables:

* **Model fidelity (number of steps)**
* **Underlying stock price**
* **Volatility**

The scripts leverage **Pascal’s Triangle** to calculate binomial probabilities, and **NumPy** + **Matplotlib** for numerical computation and visualization.

---

## 🧩 Project Overview

The **Binomial Options Pricing Model (BOPM)** approximates the fair value of options by simulating possible paths an asset’s price may take before expiration. It assumes:

* The asset price can move **up** or **down** each step.
* The probabilities of those moves are derived from the **risk-neutral probability** ( p = \frac{(1 + r \Delta t) - d}{u - d} ).
* The model discounts expected payoffs back to the present using the **risk-free rate**.

Each script isolates and visualizes how the **option’s theoretical price** changes as one key variable is altered.

---

## ⚙️ Scripts

### 1. `fidelity_vs_price.py`

**Purpose:**
Analyzes how increasing the **fidelity** (number of binomial steps) affects calculated option values.

**Plot:**
📊 *Fidelity vs Call/Put Prices*

**Key Parameters:**

* `fidelity`: 1 → 256
* `stock_price`: fixed at 230
* `strike_price`: 240
* `volatility`: 25%
* `risk-free rate`: 4%

**Insight:**
As fidelity increases, the model converges to a stable theoretical option value — approaching the continuous-time limit.

---

### 2. `stockprice_vs_price.py`

**Purpose:**
Examines how the **option value** changes with different **underlying stock prices**, keeping strike and other parameters constant.

**Plot:**
📊 *Stock Price vs Call/Put Prices*

**Key Parameters:**

* `stock_price`: 200 → 280
* `strike_price`: 240
* `volatility`: 25%
* `fidelity`: 256 steps
* `risk-free rate`: 4%

**Insight:**
Call option values rise as the stock price increases, while put option values decline — consistent with option payoff behavior.

---

### 3. `volatility_vs_price.py`

**Purpose:**
Explores how **option value** responds to changes in **volatility**, demonstrating the “vega” effect.

**Plot:**
📊 *Volatility vs Call/Put Prices*

**Key Parameters:**

* `volatility`: 0.1 → 100 (incremented by 0.1)
* `stock_price`: 250
* `strike_price`: 240
* `fidelity`: 256
* `risk-free rate`: 4%

**Insight:**
Higher volatility increases both call and put values — reflecting the market’s pricing of uncertainty.

---

## 🧮 Core Logic

Each script follows these key computational steps:

1. **Define Inputs:**
   Stock price, strike price, volatility, interest rate, time to expiry, and number of steps.

2. **Calculate Binomial Parameters:**

   * Upward factor: ( u = (1 + \sigma)^{1/N} )
   * Downward factor: ( d = 1/u )
   * Risk-neutral probability: ( p = \frac{(1 + r \Delta t) - d}{u - d} )

3. **Generate Pascal’s Triangle Row:**
   Used to determine the number of possible paths with a given number of up moves.

4. **Compute Terminal Prices:**
   ( S_T = S_0 \times u^i \times d^{N - i} )

5. **Compute Payoffs:**

   * Call: ( \max(0, S_T - K) )
   * Put: ( \max(0, K - S_T) )

6. **Calculate Expected Value:**
   Weighted by binomial probabilities derived from Pascal’s Triangle.

7. **Discount to Present:**
   Divide by ( (1 + r)^{T} ) to obtain the present value.

---

## 📦 Dependencies

```bash
pip install numpy matplotlib
```

---

## ▶️ Running the Scripts

Each script is standalone and can be run directly:

```bash
python fidelity_vs_price.py
python stockprice_vs_price.py
python volatility_vs_price.py
```

Each program outputs:

* A Matplotlib plot visualizing call and put price behavior.
* Intermediate model details (probabilities, terminal values, and discount factors) printed to console.

---

## 📉 Example Output

Example plot from `stockprice_vs_price.py`:

```
📊 Stock Price vs $ @ Fixed Strike
Call and Put Prices
```

The x-axis represents stock price, while the y-axis represents the theoretical option price under the binomial model.

---

## 📚 Concepts Illustrated

* Risk-neutral valuation
* Pascal’s Triangle & binomial coefficients
* Convergence of discrete models
* Sensitivity to volatility (Vega)
* Option pricing dynamics

---

## 🧠 Future Work

* Add comparison to **Black-Scholes** analytical model
* Extend to **American options** (early exercise)
* Integrate Monte Carlo simulations for validation
* Package as a reusable module

---

## ✍️ Author

**Nico Moran**
📧 [nxcomoran@gmail.com](mailto:nxcomoran@gmail.com)
📆 Created: 2025
🧮 Focus: Quantitative Finance, Derivatives, and Computational Modeling
