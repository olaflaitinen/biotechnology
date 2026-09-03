<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from NOTATION.md.
  Edit the source and run `make docs`.
-->

# Notation

Symbols, units, and the documentation contract every formula module must
satisfy.

This document is normative for anything under `src/biotechnology/formulas/` and
for every `Metric.symbol` and `Metric.unit` in the taxonomy.

---

## 1. Why ASCII

Every symbol stored in this library is written in **ASCII**.

`mu`, not `μ`. `t_half`, not `t½`. `1e14`, not `10¹⁴`. `Delta_Delta_Ct`, not
`ΔΔCt`.

The same string has to survive:

- a terminal with a legacy code page;
- a CSV opened in a spreadsheet that guessed the encoding wrong;
- a LaTeX document, where `μ` outside math mode is an error;
- an HTML page;
- a `grep` written by someone who cannot type Greek.

Pretty rendering is **generated at display time** from the lookup table in
`src/biotechnology/core/text.py`, never stored in the data. That table maps
`"mu"` to `μ` for HTML, `\mu` for LaTeX, and leaves it as `mu` for plain text.

```python
from biotechnology.core.text import render_symbol

render_symbol("mu")                      # 'mu'
render_symbol("mu", target="unicode")    # 'μ'
render_symbol("mu", target="latex")      # '\\mu'
```

---

## 2. Greek letters

| ASCII | Unicode | LaTeX | Conventional meaning in this library |
|-------|---------|-------|--------------------------------------|
| `alpha` | α | `\alpha` | significance level; selection differential coefficient |
| `beta` | β | `\beta` | type II error rate |
| `gamma` | γ | `\gamma` | shear rate |
| `Delta` | Δ | `\Delta` | a difference |
| `epsilon` | ε | `\epsilon` | molar extinction coefficient |
| `eta` | η | `\eta` | efficiency; dynamic viscosity |
| `theta` | θ | `\theta` | angle; dimensionless temperature |
| `kappa` | κ | `\kappa` | Cohen's kappa |
| `lambda` | λ | `\lambda` | wavelength; decay constant |
| `mu` | μ | `\mu` | specific growth rate; micro- prefix; population mean |
| `mu_max` | μ_max | `\mu_{max}` | maximum specific growth rate |
| `nu` | ν | `\nu` | kinematic viscosity |
| `pi` | π | `\pi` | osmotic pressure; the constant |
| `rho` | ρ | `\rho` | density |
| `sigma` | σ | `\sigma` | standard deviation; surface tension |
| `tau` | τ | `\tau` | residence time; shear stress |
| `phi` | φ | `\phi` | porosity; quantum yield |
| `chi2` | χ² | `\chi^2` | chi-squared statistic |
| `omega` | ω | `\omega` | angular velocity |

Where a Greek letter has more than one meaning, the formula module states which
one it uses in `notation.py`. Ambiguity is resolved locally, never globally.

---

## 3. Subscripts, superscripts and operators

| Written | Means |
|---------|-------|
| `x_i` | subscript i |
| `mu_max` | subscript max |
| `t_half` | subscript ½ - spelled out, because `t_1/2` reads as a division |
| `C_p` | subscript p |
| `x^2` | superscript 2, in prose only |
| `1e14` | 1 × 10¹⁴ - the only permitted form in a data field |
| `2.5e-3` | 2.5 × 10⁻³ |
| `10^14` | permitted in **prose**, never in a `Metric` field |
| `<`, `>`, `<=`, `>=` | comparisons; never `≤` or `≥` |
| `-` | ranges: `"1e11 - 2e14"`, spaced |
| `x` | multiplication in a range: `"5 - 30 x 10^6 cells/mL"` |

---

## 4. Units

### 4.1 Rules

1. **SI by default.** Metre, kilogram, second, mole, kelvin, ampere, candela
   and their coherent derivatives.
2. **Field convention where SI is not what practitioners use.** `vg/kg`,
   `CFU/g`, `pg/cell/day`, `copies/diploid genome`, `spores/mL`. Forcing SI
   here would make the data unrecognisable to the people who need to check it.
3. **`Metric.unit` is written out; `Metric.symbol` is abbreviated.**

   ```python
   Metric(
       name="Product titre",
       symbol="C_p",
       unit="grams per litre of harvested culture",   # written out
       typical="1 - 10 g/L for CHO fed-batch",        # abbreviated in prose
   )
   ```

4. **Dimensionless quantities** use `"-"` or `"dimensionless"`. Never leave
   `unit` empty.
5. **Per-something units** use a solidus: `1/h`, `mg/L`, `L/h`, `kg N/ha/year`.
   Not `h^-1`.

### 4.2 Prefixes

| Prefix | ASCII | Factor |
|--------|-------|--------|
| pico | `p` | 1e-12 |
| nano | `n` | 1e-9 |
| micro | `u` | 1e-6 - `u`, not `µ`, in unit strings |
| milli | `m` | 1e-3 |
| kilo | `k` | 1e3 |
| mega | `M` | 1e6 |
| giga | `G` | 1e9 |

`ug/g` means micrograms per gram. The `u` is deliberate: `µ` is a different
code point from `μ` and the two are routinely confused by text pipelines.

### 4.3 Unit checking

`src/biotechnology/core/units.py` parses these strings and can convert between
compatible ones. A formula that accepts a quantity in the wrong unit must raise
`UnitError`, never coerce silently.

```python
from biotechnology.core.units import convert
convert(1.0, "g/L", "mg/mL")     # 1.0
convert(1.0, "g/L", "1/h")       # UnitError: incompatible dimensions
```

---

## 5. The formula module contract

Every formula is a **package** of four files.

```
src/biotechnology/formulas/herd_immunity_threshold/
├── __init__.py         exports FORMULA (metadata) and the callable
├── notation.py         symbols, units, domain of validity
├── derivation.py       where the relationship comes from, with citation
└── implementation.py   the function, with doctests
```

### 5.1 `notation.py`

Declares every symbol the formula uses, with its unit and its permitted range.

```python
SYMBOLS = (
    Symbol("R0",  "basic reproduction number", "dimensionless", "> 1"),
    Symbol("H_c", "herd immunity threshold",   "fraction",      "0 - 1"),
)
```

### 5.2 `derivation.py`

States the relationship in ASCII, then in LaTeX, then explains where it comes
from and what it assumes.

```
        H_c = 1 - 1 / R0

LaTeX:  H_c = 1 - \frac{1}{R_0}

Assumes homogeneous mixing, a fully susceptible starting population, and
lifelong sterilising immunity. Real thresholds are higher wherever mixing is
assortative, which is why measles outbreaks occur in communities well above
the nominal 93 per cent.
```

The assumption paragraph is not optional. A formula presented without its
assumptions is a way of being wrong with more confidence.

### 5.3 `implementation.py`

- One public callable, named after the formula.
- Full type annotations; passes `mypy --strict`.
- **Validates its domain.** Raise `DomainError` naming the parameter, the value
  and the accepted range. Never let `math` raise a bare `ValueError` from
  inside somebody's pipeline.
- **Doctests are worked examples** whose numbers a reader can verify by hand or
  against the cited source.

```python
def herd_immunity_threshold(r0: float) -> float:
    """Fraction of a population that must be immune to stop sustained spread.

    Parameters
    ----------
    r0:
        Basic reproduction number. Must be greater than 1; below that the
        pathogen dies out unaided and the threshold is undefined.

    Returns
    -------
    float
        Immune fraction between 0 and 1.

    Raises
    ------
    DomainError
        If ``r0`` is not greater than 1.

    Examples
    --------
    >>> round(herd_immunity_threshold(15.0), 3)   # measles
    0.933
    >>> round(herd_immunity_threshold(2.5), 3)    # seasonal influenza
    0.6
    """
```

### 5.4 `__init__.py`

Exports a `Formula` metadata record - key, name, plain-language description,
the callable, its symbols, its citation keys and the subtypes that reference
it - so that `bt.formulas.get("herd_immunity_threshold")` returns something
self-describing.

---

## 6. Statistical and epidemiological conventions

| Symbol | Meaning | Note |
|--------|---------|------|
| `Se`, `Sp` | diagnostic sensitivity, specificity | properties of the test |
| `PPV`, `NPV` | positive, negative predictive value | depend on **prevalence** |
| `LR+`, `LR-` | positive, negative likelihood ratio | prevalence-independent |
| `RR`, `OR` | risk ratio, odds ratio | |
| `NNT` | number needed to treat | |
| `VE` | vaccine efficacy | `1 - RR` |
| `R0`, `R_e` | basic, effective reproduction number | |
| `H_c` | herd immunity threshold | |
| `CI` | confidence interval | always state the level: `95 % CI` |

The distinction between `PPV` and `Se` is the single most common source of
public confusion about testing, and every formula module that touches it says
so explicitly.

---

## 7. Bioprocess conventions

| Symbol | Meaning | Unit |
|--------|---------|------|
| `mu` | specific growth rate | `1/h` |
| `mu_max` | maximum specific growth rate | `1/h` |
| `K_s` | half-saturation constant (Monod) | `g/L` |
| `t_d` | doubling time | `h` |
| `Y_xs` | biomass yield on substrate | `g/g` |
| `Y_ps` | product yield on substrate | `g/g` |
| `q_p` | specific productivity | `pg/cell/day` |
| `C_p` | product titre | `g/L` |
| `VCD` | viable cell density | `10^6 cells/mL` |
| `IVCD` | integral of viable cell density | `10^6 cells*day/mL` |
| `kLa` | volumetric oxygen mass transfer coefficient | `1/h` |
| `OUR` | oxygen uptake rate | `mmol/L/h` |
| `D` | dilution rate (chemostat) | `1/h` |

---

## 8. Molecular biology conventions

| Symbol | Meaning | Unit |
|--------|---------|------|
| `Tm` | melting temperature | `degC` |
| `GC%` | guanine-cytosine content | `%` |
| `A260`, `A280` | absorbance at 260 / 280 nm | dimensionless |
| `Cq` | quantification cycle | cycles - `Ct` is the older synonym |
| `E` | amplification efficiency | dimensionless, `0 - 1` |
| `MOI` | multiplicity of infection | `TU/cell` |
| `VCN` | vector copy number | `copies/diploid genome` |
| `K_D` | equilibrium dissociation constant | `M` |
| `k_on`, `k_off` | association, dissociation rate constants | `1/(M*s)`, `1/s` |
| `EC50`, `IC50` | half-maximal effective, inhibitory concentration | `nM` |
| `LC50`, `LT50` | median lethal concentration, time | assay-specific, `days` |

Temperatures are written `degC` in unit strings and "degrees Celsius" in
`Metric.unit`, because `°` is not ASCII.

---

## 9. Genetics and breeding conventions

| Symbol | Meaning |
|--------|---------|
| `h2` | narrow-sense heritability |
| `H2` | broad-sense heritability |
| `R` | response to selection |
| `S` | selection differential |
| `i` | selection intensity, in standard deviations |
| `L` | generation interval, in years |
| `dG/t` | genetic gain per year |
| `Ne` | effective population size |
| `dF` | rate of inbreeding per generation |
| `GEBV` | genomic estimated breeding value |
| `r_gy` | prediction accuracy |
| `D'`, `r2` | linkage disequilibrium measures |

The breeder's equation, `R = h2 * S`, is written with `*` explicit. Implicit
multiplication is never used in this library, in any field, because it does not
survive being pasted into a calculator.
