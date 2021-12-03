<template>
	<div id="searchbox">
		<table style="margin: auto">
			<tr>
				<td>
					<div id="searchbox_theme" style="float: left;width:120px;">
						<el-select v-model="theme" placeholder="检索范围" class="select-options">
							<el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
							</el-option>
						</el-select>
					</div>
				</td>
				<td>
					<div id="searchbox_keywords" style="float:left;width:650px;">
						<el-input placeholder="" v-model="keyword" @keyup.enter.native="search" clearable autofocus class="input-with-select">
						<el-button style="background-color:cornflowerblue;color:cornsilk;width:60px;height:55px" @click="search" slot="append" icon="el-icon-search"></el-button>
						</el-input>
					</div>
				</td>
			</tr>
			<tr>
				<td>
					<div style="width: 120px;float:left"></div>
					</td>
				<td>
					<div style="width:390px;float:left">
						<section class="main" v-show="this.suggestList.length != 0 && this.keyword.length != 0">
							<ul class="todo-list">
								<li class="todo" v-for="(item, index) in suggestList">
									<div class="view" @click="add(index)">
										<label>{{ item }}</label>
									</div>
								</li>
							</ul>
						</section>
					</div>
				</td>

			</tr>
		</table>
	</div>
	<!-- 搜索建议 -->
</template>
<script>
	export default {
		name: "searchwindows",
		data() {
			return {
				keyword: "",
				userClick: false,
				//  总数据
				suggestList: [],
				//  输入的内容
				inputValue: "",
				theme: "",
				options: [{
						value: "",
						label: "不限",
					},
					{
						value: "name",
						label: "姓名",
					},
					{
						value: "institution",
						label: "机构",
					},
					{
						value: "field",
						label: "领域",
					},
          {
						value: "paper",
						label: "论文",
					},
				],
				value: "",
			};
		},
		watch: {
			keyword: function(val, oldVal) {
				console.log("new: %s, old: %s", val, oldVal);
				this.getsuggests();
			},
		},
		methods: {
			deletsuggestlist() {
				this.suggestList = [];
			},
			add: function(index) {
				// console.log("选中");
				// console.log(index);
				this.keyword = this.suggestList[index];
				this.suggestList = [];
			},
			getsuggests() {
				this.axios
					//.get("http://39.96.43.48/suggestion?keyword=" + this.keyword)
          .get("../../static/mock/index1.json")//Belle
					.then((response) => {
						// console.log(response);
						this.suggestList = [];
						var result = response.data;
						if (result.length === 1 && result[0].value === this.keyword) {} else {//我不理解，你要返回什么数据？？
							for (var j = 0; j < result.length; j++) {
								this.suggestList.push(result[j].value);
							}
						}

						// this.info = JSON.parse(response.data.info);
						// this.info = response.data.data.result.splice(val * 10, 10);
						// this.loading = false;
					});
			},

			search() {
				if (
					this.keyword === "" ||
					this.keyword === undefined ||
					this.keyword === null
				) {
					this.$message("搜索关键字不能为空。");
					return;
				}

				// this.$store.dispatch('showLoading')
				console.log(this.options.value);
				this.$router.push({
					path: "/search",
					query: {
						keyword: this.keyword,
						theme: this.theme
					},
				});
			},
		},
		mounted() {
			const queries = this.$route.query;
			if (queries.hasOwnProperty("keyword")) {
				this.keyword = queries.keyword;
			}
		},
	};
</script>

<style scoped>
	.select-options>>>.el-input__inner{
                                font-size:22px;
                                height:55px;
                 }
	.input-with-select .el-input-group__prepend {
		background-color: #fff;
	}
                .input-with-select>>>.el-input__inner{
                                font-size:22px;
                                height:55px;
                                width:690px;
                }

	#searchbox {
		width: 45%;
		max-width: 2200px;
		margin: auto;
		padding: 0%;
	}

	html,
	:focus {
		outline: 0;
	}

	.hidden {
		display: none;
	}

	#todoapp {
		background: #fff;
		margin: 180px 0 40px 0;
		position: relative;
		box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 25px 50px 0 rgba(0, 0, 0, 0.1);
	}

	#todoapp input::-webkit-input-placeholder {
		font-style: italic;
		font-weight: 300;
		color: #e6e6e6;
	}

	#todoapp input::-moz-placeholder {
		font-style: italic;
		font-weight: 300;
		color: #e6e6e6;
	}

	#todoapp input::input-placeholder {
		font-style: italic;
		font-weight: 300;
		color: gray;
	}

	#todoapp h1 {
		position: absolute;
		top: -160px;
		width: 100%;
		font-size: 60px;
		font-weight: 100;
		text-align: center;
		color: rgba(175, 47, 47, 0.8);
		-webkit-text-rendering: optimizeLegibility;
		-moz-text-rendering: optimizeLegibility;
		text-rendering: optimizeLegibility;
	}

	.new-todo,
	.edit {
		position: relative;
		margin: 0;
		width: 100%;
		font-size: 24px;
		font-family: inherit;
		font-weight: inherit;
		line-height: 1.4em;
		border: 0;
		color: inherit;
		padding: 6px;
		border: 1px solid #999;
		box-shadow: inset 0 -1px 5px 0 rgba(0, 0, 0, 0.2);
		box-sizing: border-box;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
	}

	.new-todo {
		padding: 16px;
		border: none;
		background: rgba(0, 0, 0, 0.003);
		box-shadow: inset 0 -2px 1px rgba(0, 0, 0, 0.03);
	}

	.main {
		position: relative;
		z-index: 2;
		border-top: 1px solid #e6e6e6;
		border-left: 1px solid #999;
		border-right: 1px solid #999;
		border-bottom: 1px solid #999;
		border-radius: 10px;
	}

	.toggle-all {
		width: 1px;
		height: 1px;
		border: none;
		/* Mobile Safari */
		opacity: 0;
		position: absolute;
		right: 100%;
		bottom: 100%;
	}

	.toggle-all+label {
		width: 60px;
		height: 34px;
		font-size: 0;
		position: absolute;
		top: -52px;
		left: -13px;
		-webkit-transform: rotate(90deg);
		transform: rotate(90deg);
	}

	.toggle-all+label:before {
		content: "❯";
		font-size: 22px;
		color: #e6e6e6;
		padding: 10px 27px 10px 27px;
	}

	.toggle-all:checked+label:before {
		color: #737373;
	}

	.todo-list {
		margin: 0;
		padding: 0;
		list-style: none;
		max-height: 420px;
		overflow: auto;
	}

	.todo-list li {
		position: relative;
		font: 400 13.3333px Arial;
		border-bottom: 1px solid #ededed;
		box-sizing: border-box;
	}

	.todo-list li:last-child {
		border-bottom: none;
	}

	.todo-list .view .index {
		position: absolute;
		color: gray;
		left: 10px;
		top: 20px;
		font-size: 16px;
	}

	.todo-list li .toggle {
		text-align: center;
		width: 40px;
		/* auto, since non-WebKit browsers doesn't support input styling */
		height: auto;
		position: absolute;
		top: 0;
		bottom: 0;
		margin: auto 0;
		border: none;
		/* Mobile Safari */
		-webkit-appearance: none;
		appearance: none;
	}

	.todo-list li .toggle {
		opacity: 0;
	}

	.todo-list li .toggle+label {
		/*
		Firefox requires `#` to be escaped - https://bugzilla.mozilla.org/show_bug.cgi?id=922433
		IE and Edge requires *everything* to be escaped to render, so we do that instead of just the `#` - https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/7157459/
	*/
		background-image: url("data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2240%22%20height%3D%2240%22%20viewBox%3D%22-10%20-18%20100%20135%22%3E%3Ccircle%20cx%3D%2250%22%20cy%3D%2250%22%20r%3D%2250%22%20fill%3D%22none%22%20stroke%3D%22%23ededed%22%20stroke-width%3D%223%22/%3E%3C/svg%3E");
		background-repeat: no-repeat;
		background-position: center left;
	}

	.todo-list li .toggle:checked+label {
		background-image: url("data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2240%22%20height%3D%2240%22%20viewBox%3D%22-10%20-18%20100%20135%22%3E%3Ccircle%20cx%3D%2250%22%20cy%3D%2250%22%20r%3D%2250%22%20fill%3D%22none%22%20stroke%3D%22%23bddad5%22%20stroke-width%3D%223%22/%3E%3Cpath%20fill%3D%22%235dc2af%22%20d%3D%22M72%2025L42%2071%2027%2056l-4%204%2020%2020%2034-52z%22/%3E%3C/svg%3E");
	}

	.todo-list li label {
		word-break: break-all;
		padding: 10px 10px 10px 30px;
		display: block;
		line-height: 1.2;
		transition: color 0.4s;
	}

	.todo-list li.completed label {
		color: #d9d9d9;
		text-decoration: line-through;
	}

	.todo-list li .destroy {
		display: none;
		position: absolute;
		top: 0;
		right: 10px;
		bottom: 0;
		width: 40px;
		height: 40px;
		margin: auto 0;
		font-size: 30px;
		color: #cc9a9a;
		margin-bottom: 11px;
		transition: color 0.2s ease-out;
	}

	.todo-list li .destroy:hover {
		color: #af5b5e;
	}

	.todo-list li .destroy:after {
		content: "×";
	}

	.todo-list li:hover .destroy {
		display: block;
	}

	.todo-list li .edit {
		display: none;
	}

	.todo-list li.editing:last-child {
		margin-bottom: -1px;
	}

	.footer {
		color: #777;
		padding: 10px 15px;
		height: 20px;
		text-align: center;
		border-top: 1px solid #e6e6e6;
	}

	.footer:before {
		content: "";
		position: absolute;
		right: 0;
		bottom: 0;
		left: 0;
		height: 50px;
		overflow: hidden;
		box-shadow: 0 1px 1px rgba(0, 0, 0, 0.2), 0 8px 0 -3px #f6f6f6,
			0 9px 1px -3px rgba(0, 0, 0, 0.2), 0 16px 0 -6px #f6f6f6,
			0 17px 2px -6px rgba(0, 0, 0, 0.2);
	}

	.todo-count {
		float: left;
		text-align: left;
	}

	.todo-count strong {
		font-weight: 300;
	}

	.filters {
		margin: 0;
		padding: 0;
		list-style: none;
		position: absolute;
		right: 0;
		left: 0;
	}

	.filters li {
		display: inline;
	}

	.filters li a {
		color: inherit;
		margin: 3px;
		padding: 3px 7px;
		text-decoration: none;
		border: 1px solid transparent;
		border-radius: 3px;
	}

	.filters li a:hover {
		border-color: rgba(175, 47, 47, 0.1);
	}

	.filters li a.selected {
		border-color: rgba(175, 47, 47, 0.2);
	}

	.clear-completed,
	html .clear-completed:active {
		float: right;
		position: relative;
		line-height: 20px;
		text-decoration: none;
		cursor: pointer;
	}

	.clear-completed:hover {
		text-decoration: underline;
	}

	.info {
		margin: 50px auto 0;
		color: #bfbfbf;
		font-size: 15px;
		text-shadow: 0 1px 0 rgba(255, 255, 255, 0.5);
		text-align: center;
	}

	.info p {
		line-height: 1;
	}

	.info a {
		color: inherit;
		text-decoration: none;
		font-weight: 400;
	}

	.info a:hover {
		text-decoration: underline;
	}

	/*
	Hack to remove background from Mobile Safari.
	Can't use it globally since it destroys checkboxes in Firefox
*/
	@media screen and (-webkit-min-device-pixel-ratio: 0) {

		.toggle-all,
		.todo-list li .toggle {
			background: none;
		}

		.todo-list li .toggle {
			height: 40px;
		}
	}

	@media (max-width: 430px) {
		.footer {
			height: 50px;
		}

		.filters {
			bottom: 10px;
		}
	}
</style>
