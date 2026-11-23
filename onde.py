"""
Onde progressive sinusoïdale
----------------------------
Simule une onde y(x, t) = A.sin(wt - kx) qui se propage le long d'une corde.
Affiche ses caractéristiques (T, lambda, w, k) et trace :
  1) l'aspect de la corde à plusieurs instants (périodicité spatiale)
  2) le mouvement de plusieurs points de la corde (périodicité temporelle)

Auteur : Mohamed Islam SAIMI
"""

import numpy as np
import matplotlib.pyplot as plt

# ---- Paramètres de l'onde ----
A = 0.02     # amplitude (m)
f = 2.0      # fréquence (Hz)
v = 4.0      # vitesse de propagation (m/s)


def caracteristiques(f, v):
    """Calcule la période, la longueur d'onde, la pulsation et le nombre d'onde."""
    T = 1 / f                 # période (s)
    lam = v / f               # longueur d'onde (m)  : v = lambda * f
    w = 2 * np.pi * f         # pulsation (rad/s)
    k = 2 * np.pi / lam       # nombre d'onde (rad/m)
    return T, lam, w, k


def onde(x, t, A, w, k):
    """Élongation y(x, t) d'une onde progressive se propageant vers les x croissants."""
    return A * np.sin(w * t - k * x)


def dephasage(d, lam):
    """Déphasage (en rad) entre deux points de la corde séparés de d."""
    return 2 * np.pi * d / lam


def main():
    T, lam, w, k = caracteristiques(f, v)
    print(f"Période           T      = {T:.3f} s")
    print(f"Longueur d'onde   lambda = {lam:.3f} m")
    print(f"Pulsation         w      = {w:.3f} rad/s")
    print(f"Nombre d'onde     k      = {k:.3f} rad/m")
    print(f"Vérification      w / k  = {w / k:.3f} m/s (= v)\n")

    for d in [lam / 2, lam]:
        phi = dephasage(d, lam)
        etat = "en opposition de phase" if np.isclose(phi % (2 * np.pi), np.pi) else "en phase"
        print(f"Points séparés de {d:.2f} m : déphasage = {phi / np.pi:.0f}π rad -> {etat}")

    fig, axes = plt.subplots(2, 1, figsize=(9, 7))

    # 1) Aspect de la corde à différents instants : y en fonction de x
    x = np.linspace(0, 3 * lam, 600)
    for t, nom in [(0, "t = 0"), (T / 4, "t = T/4"), (T / 2, "t = T/2")]:
        axes[0].plot(x, onde(x, t, A, w, k), label=nom)
    axes[0].set_title("Aspect de la corde : l'onde avance vers la droite")
    axes[0].set_xlabel("Position x (m)")
    axes[0].annotate("", xy=(lam, A * 1.25), xytext=(0, A * 1.25),
                     arrowprops=dict(arrowstyle="<->"))
    axes[0].text(lam / 2, A * 1.32, "λ", ha="center")
    axes[0].set_ylim(-A * 1.4, A * 2.1)

    # 2) Mouvement de trois points de la corde : y en fonction de t
    t = np.linspace(0, 3 * T, 600)
    for xp, nom in [(0, "x = 0"), (lam / 2, "x = λ/2"), (lam, "x = λ")]:
        style = "--" if xp == lam else "-"
        axes[1].plot(t, onde(xp, t, A, w, k), style, label=nom)
    axes[1].set_title("Mouvement de trois points de la corde (ils oscillent sur place)")
    axes[1].set_xlabel("Temps t (s)")
    axes[1].set_ylim(-A * 1.4, A * 2.1)

    for ax in axes:
        ax.set_ylabel("Élongation y (m)")
        ax.axhline(0, color="black", linewidth=0.6)
        ax.legend(loc="upper right", ncol=3)
        ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("resultat.png", dpi=120)
    plt.show()


if __name__ == "__main__":
    main()
