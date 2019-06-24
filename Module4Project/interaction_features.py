# split the ages

origin_1 = data_fin[data_fin["origin"] == 1]
origin_2 = data_fin[data_fin["origin"] == 2]
origin_3 = data_fin[data_fin["origin"] == 3]
origin_1.head()

# regress

regression_1 = LinearRegression()
regression_2 = LinearRegression()
regression_3 = LinearRegression()

horse_1 = origin_1["horse"].values.reshape(-1, 1)
horse_2 = origin_2["horse"].values.reshape(-1, 1)
horse_3 = origin_3["horse"].values.reshape(-1, 1)

regression_1.fit(horse_1, origin_1["mpg"])
regression_2.fit(horse_2, origin_2["mpg"])
regression_3.fit(horse_3, origin_3["mpg"])

# Make predictions using the testing set
pred_1 = regression_1.predict(horse_1)
pred_2 = regression_2.predict(horse_2)
pred_3 = regression_3.predict(horse_3)

# The coefficients
print(regression_1.coef_)
print(regression_2.coef_)
print(regression_3.coef_)

# plot

# Plot outputs
plt.figure(figsize=(10, 6))

plt.scatter(horse_1, origin_1["mpg"], color="blue", alpha=0.3, label="origin = 1")
plt.scatter(horse_2, origin_2["mpg"], color="red", alpha=0.3, label="origin = 2")
plt.scatter(horse_3, origin_3["mpg"], color="orange", alpha=0.3, label="origin = 3")

plt.plot(horse_1, pred_1, color="blue", linewidth=2)
plt.plot(horse_2, pred_2, color="red", linewidth=2)
plt.plot(horse_3, pred_3, color="orange", linewidth=2)
plt.ylabel("mpg")
plt.xlabel("horsepower")
plt.legend()

# cross validate

regression = LinearRegression()
crossvalidation = KFold(n_splits=3, shuffle=True, random_state=1)

X_interact = X.copy()
X_interact["horse_origin"] = X["horse"] * X["origin"]

interact_horse_origin = np.mean(
    cross_val_score(regression, X_interact, y, scoring="r2", cv=crossvalidation)
)
interact_horse_origin

import statsmodels.api as sm

X_interact = sm.add_constant(X_interact)
model = sm.OLS(y, X_interact)
results = model.fit()

results.summary()


### young vs old

yr_old = data_fin[:180]  # cars from 70 to 75
yr_young = data_fin[180:]  # cars from 76 to 82

plt.figure(figsize=(12, 7))

regression_1 = LinearRegression()
regression_2 = LinearRegression()

horse_1 = yr_old["horse"].values.reshape(-1, 1)
horse_2 = yr_young["horse"].values.reshape(-1, 1)

regression_1.fit(horse_1, yr_old["mpg"])
regression_2.fit(horse_2, yr_young["mpg"])

# Make predictions using the testing set
pred_1 = regression_1.predict(horse_1)
pred_2 = regression_2.predict(horse_2)

# The coefficients
print(regression_1.coef_)
print(regression_2.coef_)

# Plot outputs
plt.figure(figsize=(10, 6))

plt.scatter(horse_1, yr_old["mpg"], color="blue", alpha=0.3, label="older cars")
plt.scatter(horse_2, yr_young["mpg"], color="red", alpha=0.3, label="younger cars")

plt.plot(horse_1, pred_1, color="blue", linewidth=2)
plt.plot(horse_2, pred_2, color="red", linewidth=2)

plt.ylabel("mpg")
plt.xlabel("horsepower")
plt.legend()

regression = LinearRegression()
crossvalidation = KFold(n_splits=3, shuffle=True, random_state=1)

X_interact_2 = X.copy()
X_interact_2["horse_year"] = X["horse"] * X["model year"]

interact_horse_origin = np.mean(
    cross_val_score(regression, X_interact_2, y, scoring="r2", cv=crossvalidation)
)
interact_horse_origin

import statsmodels.api as sm

X_interact_2 = sm.add_constant(X_interact_2)
model = sm.OLS(y, X_interact_2)
results = model.fit()

results.summary()


from itertools import combinations

combinations = list(combinations(boston.feature_names, 2))

interactions = []
data = df.copy()
for comb in combinations:
    data["interaction"] = data[comb[0]] * data[comb[1]]
    score = np.mean(
        cross_val_score(regression, data, y, scoring="r2", cv=crossvalidation)
    )
    if score > baseline:
        interactions.append((comb[0], comb[1], round(score, 3)))

print(
    "Top 3 interactions: %s"
    % sorted(interactions, key=lambda inter: inter[2], reverse=True)[:5]
)


### build interaction model

rm = np.asarray(df[["RM"]]).reshape(len(df[["RM"]]))

high_rm = all_data[rm > np.percentile(rm, 67)]
med_rm = all_data[(rm > np.percentile(rm, 33)) & (rm <= np.percentile(rm, 67))]
low_rm = all_data[rm <= np.percentile(rm, 33)]


def build_interaction_rm(varname, description):
    regression_h = LinearRegression()
    regression_m = LinearRegression()
    regression_l = LinearRegression()
    regression_h.fit(high_rm[varname].values.reshape(-1, 1), high_rm["target"])
    regression_m.fit(med_rm[varname].values.reshape(-1, 1), med_rm["target"])
    regression_l.fit(low_rm[varname].values.reshape(-1, 1), low_rm["target"])

    # Make predictions using the testing set
    pred_high = regression_h.predict(high_rm[varname].values.reshape(-1, 1))
    pred_med = regression_m.predict(med_rm[varname].values.reshape(-1, 1))
    pred_low = regression_l.predict(low_rm[varname].values.reshape(-1, 1))

    # The coefficients
    print(regression_h.coef_)
    print(regression_m.coef_)
    print(regression_l.coef_)

    # Plot outputs
    plt.figure(figsize=(12, 7))
    plt.scatter(
        high_rm[varname], high_rm["target"], color="blue", alpha=0.3, label="more rooms"
    )
    plt.scatter(
        med_rm[varname], med_rm["target"], color="red", alpha=0.3, label="medium rooms"
    )
    plt.scatter(
        low_rm[varname],
        low_rm["target"],
        color="orange",
        alpha=0.3,
        label="low amount of rooms",
    )

    plt.plot(low_rm[varname], pred_low, color="orange", linewidth=2)
    plt.plot(med_rm[varname], pred_med, color="red", linewidth=2)
    plt.plot(high_rm[varname], pred_high, color="blue", linewidth=2)
    plt.ylabel("house value")
    plt.xlabel(description)
    plt.legend()


build_interaction_rm("LSTAT", "% of lower status")


# final model

regression = LinearRegression()
crossvalidation = KFold(n_splits=10, shuffle=True, random_state=1)

df_inter = df.copy()
df_inter["RM_LSTAT"] = df["RM"] * df["LSTAT"]
df_inter["RM_TAX"] = df["RM"] * df["TAX"]
df_inter["RM_RAD"] = df["RM"] * df["RAD"]

final_model = np.mean(
    cross_val_score(regression, df_inter, y, scoring="r2", cv=crossvalidation)
)

import statsmodels.api as sm

df_inter_sm = sm.add_constant(df_inter)
model = sm.OLS(y, df_inter_sm)
results = model.fit()

results.summary()
