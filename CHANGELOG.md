# Changelog

## 0.10.0 (2026-02-25)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/kater-ai/kater-python-sdk/compare/v0.9.0...v0.10.0)

### Features

* **cli,compiler,cache:** add `kater run` command, SDK 0.9 combinatio… ([03390ec](https://github.com/kater-ai/kater-python-sdk/commit/03390ec00cb8deb5be8b85906ed4dabb43b92779))
* **compiler,api,cli:** auto-fix broken refs when developers rename o… ([4a670d4](https://github.com/kater-ai/kater-python-sdk/commit/4a670d492d340693f1c3134fd26739681f4ab90e))
* **compiler,attributes:** tenant user attribute system + compiler access filter enforcement ([17d91f7](https://github.com/kater-ai/kater-python-sdk/commit/17d91f799667bfc62df863a9ab0555e657108764))
* **compiler:** add per-tenant isolation support across compiler and … ([c9911f7](https://github.com/kater-ai/kater-python-sdk/commit/c9911f7e15b3e9d7657152ead4a8b00f7f6ead37))
* feat(all) updated file structures ([e0628b6](https://github.com/kater-ai/kater-python-sdk/commit/e0628b65e940423fd319a4804e6046cc519d23dd))
* feat/yvonne ([840f1f2](https://github.com/kater-ai/kater-python-sdk/commit/840f1f212abb52a6119fb5a44925926c4a157f4d))
* Feat/yvonne ([a56420e](https://github.com/kater-ai/kater-python-sdk/commit/a56420eec8d563237dfa05e2127e158bc98050eb))
* **sandbox:** query gallery, manifest lookup, and compiler updates ([1fde3d7](https://github.com/kater-ai/kater-python-sdk/commit/1fde3d7b736912cf94c85d5ff16c8d4be46404e4))
* **schema,compiler:** remove dynamic filters, extend variable system… ([4fcd3d9](https://github.com/kater-ai/kater-python-sdk/commit/4fcd3d9f52ca67f9b6946bf5afb06b97c83ac444))


### Bug Fixes

* address PR feedback and resolve errors (iteration 1) ([de9fb61](https://github.com/kater-ai/kater-python-sdk/commit/de9fb61cbe1973284c98f140647bda096da49b2c))
* address PR feedback and resolve errors (iteration 1) ([8e39e50](https://github.com/kater-ai/kater-python-sdk/commit/8e39e504892c130144552872070771a7d2017416))


### Chores

* **internal:** add request options to SSE classes ([98c0598](https://github.com/kater-ai/kater-python-sdk/commit/98c0598977b4ff4968590f9c33cbdd040a6118f8))
* **internal:** make `test_proxy_environment_variables` more resilient ([a1840ec](https://github.com/kater-ai/kater-python-sdk/commit/a1840ec2a5148558b2d13b81c3a18a538d436878))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([4af645f](https://github.com/kater-ai/kater-python-sdk/commit/4af645ff03e5b0dbe161b13ed7a3c50985740d1e))
* **internal:** remove mock server code ([2f11413](https://github.com/kater-ai/kater-python-sdk/commit/2f1141377ba0117a78ebfb0e48f86bd0c6d32a24))
* update mock server docs ([377d3c6](https://github.com/kater-ai/kater-python-sdk/commit/377d3c6e6dc53f699b8d7a8ec01c4df1e308bf85))

## 0.9.0 (2026-02-14)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/kater-ai/kater-python-sdk/compare/v0.8.0...v0.9.0)

### Features

* **cache:** add pre-aggregate query cache with DuckDB backend ([ac8feb0](https://github.com/kater-ai/kater-python-sdk/commit/ac8feb062dd7559f7cd478f63f0bcdb3ddee061e))
* **compiler:** add select_from for CTE-based query composition ([ef738f1](https://github.com/kater-ai/kater-python-sdk/commit/ef738f11b331edd0237c8e3c2f8515e7839a017f))
* **compiler:** replace structured resolve fields with combination st… ([286fe57](https://github.com/kater-ai/kater-python-sdk/commit/286fe57aef3d79b2f0fce8682f08d79d51d279c2))
* feat(all) shippable widgets ([b33363a](https://github.com/kater-ai/kater-python-sdk/commit/b33363a2508788d86e0648113b48bdcf2d285b90))
* Feat/calculation widget mapping ([2a04ef7](https://github.com/kater-ai/kater-python-sdk/commit/2a04ef7a3329d7052764d428f3524a39140951d6))
* Feat/compiler widget validation ([1190e30](https://github.com/kater-ai/kater-python-sdk/commit/1190e30b04a3807cae712c548f80e0feb3bb4542))
* Feat/landing page ([9811c30](https://github.com/kater-ai/kater-python-sdk/commit/9811c305ba52f08bb755470e89b3f671125a3a38))
* **schema:** make widget_category required and add allowed_widget_ty… ([b7dcbcf](https://github.com/kater-ai/kater-python-sdk/commit/b7dcbcf5f490a50c57c4e8e1bac280d8cbfe0b13))
* **schema:** make widget_category required and add disallowed_widget… ([23b0482](https://github.com/kater-ai/kater-python-sdk/commit/23b04827be10b1f5e0ecaa4abefae1a20bfb28e3))


### Chores

* format all `api.md` files ([296d1f4](https://github.com/kater-ai/kater-python-sdk/commit/296d1f461f371058fcca46ead37030cd9b2f106d))
* **internal:** fix lint error on Python 3.14 ([93b8c09](https://github.com/kater-ai/kater-python-sdk/commit/93b8c0960fee88c96fd57a1ac7e8e0ea5f69ab9c))

## 0.8.0 (2026-02-10)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/kater-ai/kater-python-sdk/compare/v0.7.0...v0.8.0)

### Features

* **cli:** implement `kater validate` command with per-connection res… ([30620e0](https://github.com/kater-ai/kater-python-sdk/commit/30620e085104ba6405b8070217699f9355c2078e))


### Chores

* **internal:** bump dependencies ([66dd7fd](https://github.com/kater-ai/kater-python-sdk/commit/66dd7fdc0822343c8549d098f09499e7e17fbe8d))

## 0.7.0 (2026-02-10)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/kater-ai/kater-python-sdk/compare/v0.6.0...v0.7.0)

### Features

* **api:** expose tenant and tenant group schema endpoints in public API ([4eb02c3](https://github.com/kater-ai/kater-python-sdk/commit/4eb02c3a1e8c90d7dce4902375529cdce1ec9e37))
* **api:** manual updates ([04bd635](https://github.com/kater-ai/kater-python-sdk/commit/04bd63543e429ea0d11615f9ffda89810289545e))
* **api:** manual updates ([f534c3a](https://github.com/kater-ai/kater-python-sdk/commit/f534c3ae729a5a94433afcd13fb84c452f217147))
* **api:** manual updates ([e7fd1e9](https://github.com/kater-ai/kater-python-sdk/commit/e7fd1e911b46a0e5c0a886cca5df3b09ccc234b9))

## 0.6.0 (2026-02-10)

Full Changelog: [v0.5.1...v0.6.0](https://github.com/kater-ai/kater-python-sdk/compare/v0.5.1...v0.6.0)

### Features

* **api:** manual updates ([a245c4a](https://github.com/kater-ai/kater-python-sdk/commit/a245c4af66be42f56225fa7fbb0e419efaa35320))
* **api:** manual updates ([d2e3e1d](https://github.com/kater-ai/kater-python-sdk/commit/d2e3e1d7b3be8b59fd6921283d6c3b7083014a4d))
* **api:** manual updates ([7c32ece](https://github.com/kater-ai/kater-python-sdk/commit/7c32eced7c16df58a225951404973f1b3cf48ed8))
* **api:** manual updates ([985f3cb](https://github.com/kater-ai/kater-python-sdk/commit/985f3cb5388d8e181e6a8686bdba439e3985d5d3))
* **api:** manual updates ([c8a945c](https://github.com/kater-ai/kater-python-sdk/commit/c8a945cdea037b68b13025929668b2d1f9ee4ca5))


### Bug Fixes

* **api:** prune orphaned schemas and preserve auto-generated security… ([a6af3dd](https://github.com/kater-ai/kater-python-sdk/commit/a6af3dda2068cfb67bd63f857ee8eb2ee49d0c9d))


### Chores

* add internal route tagging, clean up CLI, and fix CI build issues ([3313bdc](https://github.com/kater-ai/kater-python-sdk/commit/3313bdc24743c68e0415fcf5fb12cf014c4234be))

## 0.5.1 (2026-02-09)

Full Changelog: [v0.5.0...v0.5.1](https://github.com/kater-ai/kater-python-sdk/compare/v0.5.0...v0.5.1)

## 0.5.0 (2026-02-08)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/kater-ai/kater-python-sdk/compare/v0.4.0...v0.5.0)

### Features

* added patch connection and credentials ([fdd46a3](https://github.com/kater-ai/kater-python-sdk/commit/fdd46a31386b0f73c4547191cd5eac93d246e34b))
* **api,core:** simplify connection creation and fix migration chain ([596e9d7](https://github.com/kater-ai/kater-python-sdk/commit/596e9d76b99aacc380a0e1836331a9973257ff86))
* Chore/cleanup connection models ([ad51c89](https://github.com/kater-ai/kater-python-sdk/commit/ad51c89f39a99e823020679ca5e8e0d8a97be3d3))
* **client:** add custom JSON encoder for extended type support ([2af9fb8](https://github.com/kater-ai/kater-python-sdk/commit/2af9fb811c6c09d41d75d8d870cddb13f85b3bc6))
* **core,api,web:** display real synced view files in schema sync UI ([e3421e9](https://github.com/kater-ai/kater-python-sdk/commit/e3421e97585f2bc6179caa7f9de8ae43712f50bb))
* **core,api,web:** implement async schema sync with Hatchet workflow… ([70ab7f2](https://github.com/kater-ai/kater-python-sdk/commit/70ab7f23dfb2f61bb1d39487860d303af134112e))
* **core,api:** add database_object_name field to Database and Schema ([2700d6c](https://github.com/kater-ai/kater-python-sdk/commit/2700d6c33e298112baa60913a271dc3b26f44b0a))
* **core,api:** add PR approval flow for connection creation ([22d94ac](https://github.com/kater-ai/kater-python-sdk/commit/22d94aca4238dccecec59377d92a653202ccd292))
* Feat/fix create connection fe ([79797f4](https://github.com/kater-ai/kater-python-sdk/commit/79797f4ac92048ea7b5a8d896626cd7d7bbca2dd))
* **tenants:** serve tenant and group YAML from server-side schema en… ([4918cbe](https://github.com/kater-ai/kater-python-sdk/commit/4918cbec00c6e383b9e1225fac6d971e5a184bf9))


### Chores

* **ci:** add missing environment ([83bbb43](https://github.com/kater-ai/kater-python-sdk/commit/83bbb4373a2c2813719d1760249ece795190b571))

## 0.4.0 (2026-01-29)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/kater-ai/kater-python-sdk/compare/v0.3.0...v0.4.0)

### Features

* **api:** improve OpenAPI spec generation with pre-commit validation ([bd7fb83](https://github.com/kater-ai/kater-python-sdk/commit/bd7fb83370d26957f2ace147d8544b6f78df4160))

## 0.3.0 (2026-01-28)

Full Changelog: [v0.2.1...v0.3.0](https://github.com/kater-ai/kater-python-sdk/compare/v0.2.1...v0.3.0)

### Features

* **api:** manual updates ([0a76475](https://github.com/kater-ai/kater-python-sdk/commit/0a7647569f34ae69b94fed8fc624a2f48e34a049))

## 0.2.1 (2026-01-27)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/kater-ai/kater-python-sdk/compare/v0.2.0...v0.2.1)

## 0.2.0 (2026-01-26)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/kater-ai/kater-python-sdk/compare/v0.1.0...v0.2.0)

### Features

* **api:** switch to oidc based auth ([5de423f](https://github.com/kater-ai/kater-python-sdk/commit/5de423f3de317ffa738613fd438da89df0494110))
* **api:** update stainless config ([095300b](https://github.com/kater-ai/kater-python-sdk/commit/095300b675e3e21df0aa6a0bb8cbec3d368202dd))

## 0.1.0 (2026-01-26)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/kater-ai/kater-python-sdk/compare/v0.0.1...v0.1.0)

### Features

* **api:** update auth params ([e9f46b6](https://github.com/kater-ai/kater-python-sdk/commit/e9f46b611564f4f604de6ded57d5f60a94033ab0))


### Chores

* update SDK settings ([dc43ba4](https://github.com/kater-ai/kater-python-sdk/commit/dc43ba4053472a0962b443bdbc67b16e05ede62b))
* update SDK settings ([333f170](https://github.com/kater-ai/kater-python-sdk/commit/333f170ceaac38dccd8112fcb99915667ad98330))
