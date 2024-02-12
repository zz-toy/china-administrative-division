package main

import (
	"flag"
	"fmt"
	"net/http"

	"alice/internal/config"
	"alice/internal/handler"
	"alice/internal/svc"
	"alice/internal/types"

	"github.com/zeromicro/go-zero/core/conf"
	"github.com/zeromicro/go-zero/core/logc"
	"github.com/zeromicro/go-zero/core/logx"
	"github.com/zeromicro/go-zero/rest"
	handler2 "github.com/zeromicro/go-zero/rest/handler"
	"github.com/zeromicro/go-zero/rest/httpx"
)

var configFile = flag.String("f", "etc/alice-api.yaml", "the config file")

func main() {
	flag.Parse()

	var c config.Config
	conf.MustLoad(*configFile, &c)

	server := rest.MustNewServer(
		c.RestConf,
		rest.WithCustomCors(nil, func(w http.ResponseWriter) {
			w.Header().Set("Access-Control-Allow-Origin", "*")
			w.Header().Set("Access-Control-Allow-Headers", "*")
			w.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS, PATCH")
			w.Header().Set("Access-Control-Expose-Headers", "Content-Length, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers")
			w.Header().Set("Access-Control-Allow-Credentials", "true")
		}, "*"),
		rest.WithUnauthorizedCallback(unauthorizedCallback()),
		rest.WithNotFoundHandler(notFoundHandler()),
		rest.WithNotAllowedHandler(notAllowedHandler()))
	registerStaticRoute(server)
	defer server.Stop()

	var cfg logx.LogConf = c.Log
	_ = conf.FillDefault(&cfg)
	logc.MustSetup(cfg)
	defer logc.Close()
	httpx.SetErrorHandler(errorHandler)

	ctx := svc.NewServiceContext(c)
	handler.RegisterHandlers(server, ctx)

	fmt.Printf("Starting server at %s:%d...\n", c.Host, c.Port)
	server.Start()
}

// 500
func errorHandler(err error) (int, any) {
	return http.StatusInternalServerError, types.FailResponse(http.StatusInternalServerError, err.Error())
}

// 401
func unauthorizedCallback() handler2.UnauthorizedCallback {
	return func(w http.ResponseWriter, r *http.Request, err error) {
		httpx.WriteJson(w, http.StatusUnauthorized, types.FailResponse(http.StatusUnauthorized, http.StatusText(http.StatusUnauthorized)))
		return
	}
}

// 403
func notAllowedHandler() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		httpx.WriteJson(w, http.StatusForbidden, types.FailResponse(http.StatusForbidden, http.StatusText(http.StatusForbidden)))
		return
	}
}

// 404
func notFoundHandler() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		httpx.WriteJson(w, http.StatusNotFound, types.FailResponse(http.StatusNotFound, http.StatusText(http.StatusNotFound)))
		return
	}
}

func registerStaticRoute(server *rest.Server) {
	server.AddRoute(rest.Route{
		Method:  http.MethodGet,
		Path:    "/static/:file",
		Handler: http.StripPrefix("/static/", http.FileServer(http.Dir("ui"))).ServeHTTP,
	})
}
